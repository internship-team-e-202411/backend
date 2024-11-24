import requests
import json

url = 'http://localhost:8000/add/'
headers = {'Content-Type': 'application/json'}
data = {
    "song_name": "曲名333",
    "artist_name": "アーティスト名2",
    "album_name": "アルバム名2",
    "release_date": "2024-11-01",
    "duration_ms": 1234562,
    "track_id": "トラックID2",
    "album_image_url": "アルバム画像のURL999"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
