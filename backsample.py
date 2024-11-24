import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
q="A"
client_id ="5af187ebd64a43f6814bcab19c65f922"
client_secret = "fa6277a3d46c4ffc8a0ad0f2abf8d216"
ccm = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
spotify = spotipy.Spotify(client_credentials_manager = ccm)

def get_track_data(q):
    client_id = '5af187ebd64a43f6814bcab19c65f922'
    client_secret = 'fa6277a3d46c4ffc8a0ad0f2abf8d216'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    results = spotify.search(q, limit=30, type="track", market="JP", offset=0)
    tracks = []
    for track in results["tracks"]["items"]:
        song_name = track["name"]  # 曲名
        artist_name = track["artists"][0]["name"]  # アーティスト名
        album_name = track["album"]["name"]  # アルバム名
        release_date = track["album"]["release_date"]  # リリース日
        popularity = track["popularity"]  # 人気度
        duration_ms = track["duration_ms"]  # 曲の長さ(ms)
        track_id = track["id"]  # トラックID
        preview_url = track["preview_url"]  # プレビューurl
        album_image = track["album"]["images"][0]["url"]  # アルバム画像url

        # トラックのオーディオ特徴量を取得
        audio_features = spotify.audio_features(track_id)[0]
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
            'duration_ms': duration_ms,
            'track_id': track_id,
            'album_image_url': album_image,
            # 必要に応じて他のフィールドを追加
        })
    return tracks

print(f'アーティスト名:{artist_name}曲名:{song_name} テンポ: {tempo}')