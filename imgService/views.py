from rest_framework import generics, permissions, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from imgService.permissions import IsBetaPlayerPermission
from .models import Image
from .serializers import ImageDescriptionUpdateSerializer, ImageSerializer


class ImageViewSet(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    """
        this will activate guard for all routes of this view
    """
    # permission_classes = [IsBetaPlayerPermission]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions
        that this view requires.
        """
        if self.request.method in ["POST", "DELETE"]:
            return [IsBetaPlayerPermission()]
        return [permissions.IsAuthenticated()]


class ImageDescriptionUpdateAPIView(generics.UpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageDescriptionUpdateSerializer
    permission_classes = [IsBetaPlayerPermission]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ImageSingleHandler(generics.RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def destroy(self, request, *args, **kwargs):
        print("=============== [image deleted succefully] ==============")
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        print(f"========= METHOD: [{self.request.method}] ========")

        if self.request.method in ["DELETE"]:
            return [IsBetaPlayerPermission()]
        return [permissions.IsAuthenticated()]
