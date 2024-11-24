from django.db import models

# Create your models here.
class Songs(models.Model):
    track_id = models.CharField(max_length=100, primary_key=True)   # トラックID(主キー)
    song_name = models.CharField(max_length=100)                    # 曲名
    artist_name = models.CharField(max_length=100)                  # アーティスト名
    album_name = models.CharField(max_length=100)                   # アルバム名
    release_date = models.CharField(max_length=100)                 # リリース日 (datetime?)
    popularity = models.IntegerField()                              # 人気度
    duration_ms  = models.IntegerField()                            # 曲の長さ
    preview_url  = models.CharField(max_length=500)                 # プレビューurl
    album_image  = models.CharField(max_length=500)                 # アルバム画像url
    created_at = models.DateField(auto_now_add=True)                # 作成日