from django.db import models

# Create your models here.


class KonkaniSongs(models.Model):
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    music_file = models.FileField(upload_to='KonkaniSongs/')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.album+self.artist
