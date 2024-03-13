from django.urls import path
from .views import (
    ImageDescriptionUpdateAPIView,
    ImageViewSet,
    ImageSingleHandler
)

urlpatterns = [
    path("", ImageViewSet.as_view(), name="image-list"),
    path(
        "<int:pk>/description",
        ImageDescriptionUpdateAPIView.as_view(),
        name="image-description-update",
    ),
    path(
        "<int:pk>/",
        ImageSingleHandler.as_view(),
        name="image-detail",
    ),
]
