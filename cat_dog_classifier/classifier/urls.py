from django.urls import path

from classifier.views import (
    ClassifierImageUploadView,
    ClassifierImageUploadAPIView
)

urlpatterns = (
    path(r"", ClassifierImageUploadView.as_view(), name="upload-image"),
    path(
        r"/api",
        ClassifierImageUploadAPIView.as_view(),
        name="api-upload-image"
    ),
)