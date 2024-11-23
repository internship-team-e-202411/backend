import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id =""
client_secret = ""
ccm = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
spotify = spotipy.Spotify(client_credentials_manager = ccm)

results = spotify.search(q="A", limit=100, type="track", market="JP", offset=0)
for track in results["tracks"]["items"]:
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
	
