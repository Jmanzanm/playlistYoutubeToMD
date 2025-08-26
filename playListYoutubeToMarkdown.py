import requests
import os
import re
from urllib.parse import urlparse, parse_qs

# Clave de API
API_KEY = os.getenv("YOUTUBE_API_KEY")

# Solicita la URL de la playlist
playlist_url = input("🔗 Introduce la URL de la playlist de YouTube: ").strip()

# Extrae el ID de la playlist desde la URL
parsed_url = urlparse(playlist_url)
query_params = parse_qs(parsed_url.query)
playlist_id = query_params.get("list", [None])[0]

if not playlist_id:
    print("❌ No se pudo extraer el ID de la playlist.")
    exit()

# Obtener el título de la playlist
playlist_info_url = "https://www.googleapis.com/youtube/v3/playlists"
playlist_info_params = {
    "part": "snippet",
    "id": playlist_id,
    "key": API_KEY
}
playlist_info = requests.get(playlist_info_url, params=playlist_info_params).json()

try:
    playlist_title = playlist_info["items"][0]["snippet"]["title"]
except (KeyError, IndexError):
    print("❌ No se pudo obtener el título de la playlist.")
    exit()

# Limpia el título para usarlo como nombre de archivo
playlist_title_clean = re.sub(r'[\\/*?:"<>|]', "", playlist_title)

# Obtener los videos de la playlist
url = 'https://www.googleapis.com/youtube/v3/playlistItems'
params = {
    'part': 'snippet',
    'playlistId': playlist_id,
    'maxResults': 50,
    'key': API_KEY
}
response = requests.get(url, params=params)
data = response.json()

if 'items' not in data or not data['items']:
    print("❌ No se encontraron videos o hubo un error con la API.")
    exit()

# Crear el contenido Markdown
markdown_lines = [f"# ✅ {playlist_title_clean}\n"]