from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("music_app.web.urls")),
    path("album/", include("music_app.albums.urls")),
    path("profiles/", include("music_app.profiles.urls")),
]
