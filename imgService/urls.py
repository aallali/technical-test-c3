from django.urls import path
from .views import (
    ImageDescriptionUpdateAPIView,
    ImageViewSet,
    ImageSingleHandler
)

urlpatterns = [
    path("images/", ImageViewSet.as_view(), name="image-list"),
    path(
        "images/<int:pk>/description",
        ImageDescriptionUpdateAPIView.as_view(),
        name="image-description-update",
    ),
    path(
        "images/<int:pk>/",
        ImageSingleHandler.as_view(),
        name="image-detail",
    ),
]
