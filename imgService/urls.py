from django.urls import path
from .views import ImageViewSet, ImageDetailView

urlpatterns = [
    path('images/', ImageViewSet.as_view(), name='image-list'),
    path('images/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
]
