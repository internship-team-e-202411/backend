import spotipy, webbrowser, random
from spotipy.oauth2 import SpotifyClientCredentials

client_id ="5af187ebd64a43f6814bcab19c65f922"
client_secret = "fa6277a3d46c4ffc8a0ad0f2abf8d216"
ccm = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
spotify = spotipy.Spotify(client_credentials_manager = ccm)
moji = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"

for x in range(100):
	results = spotify.search(q=moji[random.randrange(0,108)], limit=50, type="track", offset=0)
	track = results["tracks"]["items"][random.randrange(0,50)]
	song_name = track["name"] #曲名
	artist_name = track["artists"][0]["name"] #アーティスト名
	album_name = track["album"]["name"] #アルバム名
	release_date = track["album"]["release_date"] #リリース日
	popularity = track["popularity"] #人気度
	duration_ms = track["duration_ms"] #曲の長さ(ms)
	track_id = track["id"] #トラックID
	preview_url = track["preview_url"] #プレビューurl
	album_image = track["album"]["images"][0]["url"] #アルバム画像url
	print(song_name, artist_name, album_name, release_date, popularity, duration_ms, track_id, preview_url, album_image)
