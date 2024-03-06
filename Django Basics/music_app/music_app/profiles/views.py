from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from music_app.profiles.models import Profile
from music_app.web.views import get_profile


class DetailProfileView(DetailView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-details.html"

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(DeleteView):
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()
