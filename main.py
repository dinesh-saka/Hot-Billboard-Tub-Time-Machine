from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "CLIENT ID"
CLIENT_SECRET = "SECRET ID"
URI = "http://example.com"

date = input("Which year do you want to travel to? (in YYYY-MM-DD format): ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")


soup = BeautifulSoup(response.text, "html.parser")
songs = soup.select(selector="li ul li h3")
songs_list = [song.getText() for song in songs]
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                    client_secret=CLIENT_SECRET,
                                                    redirect_uri=URI,
                                                    scope="playlist-modify-private",
                                                    cache_path="token.txt",
                                                    show_dialog=True))
user_id = spotify.current_user()["id"]
song_uris = []

year = date.split("-")[0]
for song in songs_list:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = spotify.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

