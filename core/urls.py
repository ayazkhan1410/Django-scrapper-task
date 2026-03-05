from django.urls import path
from .views import ProfileCreateAPIView


urlpatterns = [
    path(
        'profiles/',
        ProfileCreateAPIView.as_view(),
    ),
]
