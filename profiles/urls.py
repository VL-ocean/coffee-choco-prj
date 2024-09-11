from django.urls import path
from .views import Profiles, EditProfile


urlpatterns = [
    path('edit/<int:pk>/', EditProfile.as_view(), name="edit_profile"),
    path('user/<int:pk>/', Profiles.as_view(), name="profile")
]