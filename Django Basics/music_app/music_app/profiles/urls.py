from django.urls import path

from music_app.profiles.views import DeleteProfileView, DetailProfileView

urlpatterns = (
    path("delete/", DeleteProfileView.as_view(), name="delete_profile"),
    path("details/", DetailProfileView.as_view(), name="details_profile")
)
