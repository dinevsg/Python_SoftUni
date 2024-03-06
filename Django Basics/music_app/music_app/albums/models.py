from django.core.validators import MinValueValidator
from django.db import models
from music_app.profiles.models import Profile


class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MIN_PRICE = 0.0
    MAX_GENRE_LENGTH = 30

    GENRE_POP_MUSIC = "Pop Music"
    GENRE_JAZZ_MUSIC = "Jazz Music"
    GENRE_ROCK_MUSIC = "Rock Music"
    GENRE_COUNTRY_MUSIC = "Country Music"
    GENRE_RNB_MUSIC = "R&B Music"
    GENRE_DANCE_MUSIC = "Dance Music"
    GENRE_HIP_HOP_MUSIC = "Hip Hop Music"
    GENRE_OTHER = "Other"

    GENRES = (
        (GENRE_POP_MUSIC, GENRE_POP_MUSIC),
        (GENRE_JAZZ_MUSIC, GENRE_JAZZ_MUSIC),
        (GENRE_ROCK_MUSIC, GENRE_ROCK_MUSIC),
        (GENRE_COUNTRY_MUSIC, GENRE_COUNTRY_MUSIC),
        (GENRE_RNB_MUSIC, GENRE_RNB_MUSIC),
        (GENRE_DANCE_MUSIC, GENRE_DANCE_MUSIC),
        (GENRE_HIP_HOP_MUSIC, GENRE_HIP_HOP_MUSIC),
        (GENRE_OTHER, GENRE_OTHER)
    )

    name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Album name"
    )

    artis_name = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False,
        verbose_name="Artist"
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL"
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE),
            ),
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=GENRES,
        null=False,
        blank=False,
    )
