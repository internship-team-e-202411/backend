from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Track
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.views.decorators.csrf import csrf_exempt
import json, random, datetime

client_id = '5af187ebd64a43f6814bcab19c65f922'
client_secret = 'fa6277a3d46c4ffc8a0ad0f2abf8d216'
moji = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"
number_of_songs = 1
def search_track(request):
    tracks = []
    for i in range(number_of_songs):
        query = moji[random.randrange(0, len(moji))]
        if query is not None:
            sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
            results = sp.search(query, limit=50, type="track", offset=0)
            track = results["tracks"]["items"][random.randrange(0, len(results["tracks"]["items"]))]
            song_name = track["name"]  # 曲名
            artist_name = track["artists"][0]["name"]  # アーティスト名
            album_name = track["album"]["name"]  # アルバム名
            release_date = track["album"]["release_date"]  # リリース日
            popularity = track["popularity"]  # 人気度
            duration_ms = track["duration_ms"]  # 曲の長さ(ms)
            track_id = track["id"]  # トラックID
            preview_url = track["preview_url"]  # プレビューurl
            album_image = track["album"]["images"][0]["url"]  # アルバム画像url

            # トラックの特徴量
            audio_features = sp.audio_features(track_id)[0]
            danceability = audio_features["danceability"]
            acousticness = audio_features["acousticness"]
            energy = audio_features["energy"]
            instrumentalness = audio_features["instrumentalness"]
            liveness = audio_features["liveness"]
            loudness = audio_features["loudness"]
            speechiness = audio_features["speechiness"]
            tempo = audio_features["tempo"]
            valence = audio_features["valence"]

            tracks.append({
                'song_name': song_name,
                'artist_name': artist_name,
                'album_name': album_name,
                'release_date': release_date,
                'popularity': popularity,
                'duration_ms': duration_ms,
                'track_id': track_id,
                'preview_url': preview_url,
                'album_image': album_image,
                'danceability': danceability,
                'acousticness': acousticness,
                'energy': energy,
                'instrumentalness': instrumentalness,
                'liveness': liveness,
                'loudness': loudness,
                'speechiness': speechiness,
                'tempo': tempo,
                'valence': valence
            })
        else:
            return JsonResponse({'error': 'No query parameter provided'}, status=400, json_dumps_params={'ensure_ascii': False})
    return JsonResponse(tracks, safe=False, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def add_track(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        track = Track(
            song_name=data['song_name'],
            artist_name=data['artist_name'],
            album_name=data['album_name'],
            release_date=data['release_date'],
            duration_ms=data['duration_ms'],
            track_id=data['track_id'],
            album_image_url=data['album_image_url']
        )
        track.save()
        return JsonResponse({'message': 'Track added successfully'}, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400, json_dumps_params={'ensure_ascii': False})
    
    
#リストから曲削除  
@csrf_exempt  
def delete_track(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        track = Track.objects.filter(track_id=data['track_id'])
        if track.exists():
            track.delete()
            return JsonResponse({'message': 'Track deleted successfully'}, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({'error': 'Track not found'}, status=404, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400, json_dumps_params={'ensure_ascii': False})

def get_track_list(request):
    tracks = Track.objects.all().values()
    return JsonResponse(list(tracks), safe=False, json_dumps_params={'ensure_ascii': False})

