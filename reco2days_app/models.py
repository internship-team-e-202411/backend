from django.db import models

class Track(models.Model):
    track_id = models.CharField(max_length=255, primary_key=True)  # 一意制約を削除
    song_name = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    duration_ms = models.IntegerField()
    album_image_url = models.URLField()
    
    def __str__(self):
        return f"{self.song_name} by {self.artist_name}"