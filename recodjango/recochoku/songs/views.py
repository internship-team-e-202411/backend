from django.shortcuts import render
from models import Songs

musics = {
    "track_id": "", 
    "song_name": , 
    "artist_name": , 
    "album_name": , 
    "release_date": ,
    "popularity": , 
    "duration_ms": , 
    "preview_url": , 
    "album_image": ,
    "created_at": ,
}

# Create your views here.
def update(request, pk):
    if request.method == "POST":
        Songs.objects.update_or_create(
            pk=pk, 
            defaults=musics,
        )