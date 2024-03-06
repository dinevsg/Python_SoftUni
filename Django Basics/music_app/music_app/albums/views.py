from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from music_app.albums.models import Album
from music_app.web.views import get_profile


class AlbumFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["name"].widget.attrs["placeholder"] = "Album Name"
        form.fields["artis_name"].widget.attrs["placeholder"] = "Artist"
        form.fields["description"].widget.attrs["placeholder"] = "Description"
        form.fields["price"].widget.attrs["placeholder"] = "Price"
        form.fields["image_url"].widget.attrs["placeholder"] = "Image URL"
        return form


class ReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"

        return form


class CreateAlbumView(AlbumFormMixin, CreateView):
    queryset = Album.objects.all()
    fields = ["name", "artis_name", "genre", "description", "image_url", "price"]
    template_name = "albums/album-add.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = get_profile()
        
        return super().form_valid(form)


class DetailAlbumView(DetailView):
    queryset = Album.objects.all()
    template_name = "albums/album-details.html"


class EditAlbumView(AlbumFormMixin, UpdateView):
    queryset = Album.objects.all()
    fields = ["name", "artis_name", "genre", "description", "image_url", "price"]
    template_name = "albums/album-edit.html"
    success_url = reverse_lazy("index")


class DeleteAlbumView(ReadOnlyMixin, DeleteView):
    queryset = Album.objects.all()
    template_name = "albums/album-delete.html"
    success_url = reverse_lazy("index")
    form_class = modelform_factory(Album, fields=["name", "artis_name", "genre", "description", "image_url", "price"])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object

        return kwargs


