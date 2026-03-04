from django.urls import path
from .views import ProfileCreateAPIView


urlpatterns = [
    path(
        'api/profiles/',
        ProfileCreateAPIView.as_view(), name='profile-create'
    ),
]
