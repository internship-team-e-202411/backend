from django.db import models

class Track(models.Model):
    song_name = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255)
    release_date = models.DateField()
    duration_ms = models.IntegerField()
    track_id = models.CharField(max_length=255)  # 一意制約を削除
    album_image_url = models.URLField()
    
    def __str__(self):
        return f"{self.song_name} by {self.artist_name}"