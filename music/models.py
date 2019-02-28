from django.db import models


class Index(models.Model):
    album_name = models.CharField(max_length=250)

    def __str__(self):
        return self.album_name


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title


class Song(models.Model):
    artist = models.CharField(max_length=250)
    song_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=10, null=True, blank=True)
    song_logo = models.CharField(max_length=1000)
    song_year = models.IntegerField(default=1992)


    def __str__(self):
        return self.song_title

class Photo(models.Model):
    artist = models.CharField(max_length=250)
    photo_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    photo_year = models.IntegerField(default=1992)

    def __str__(self):
        return self.artist

    # ------------------