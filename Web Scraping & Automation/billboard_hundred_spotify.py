from bs4 import BeautifulSoup
import spotipy
import requests
import pprint
import json
import os

date = input("Which year would you like to travel to? (YYYY-MM-DD) : ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_web_page = response.text

my_client_id = f"f{os.environ["client_id"]}"
my_client_secret = f"f{os.environ["client_secret"]}"

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'

auth = spotipy.oauth2.SpotifyOAuth(client_id=my_client_id, client_secret=my_client_secret, redirect_uri="http://example.com", scope="playlist-modify-private", cache_path="C:\\Users\\mhuz4\\OneDrive\\Desktop\\Spotify")
access_token = auth.get_access_token(as_dict=False)
spotify = spotipy.Spotify(auth=access_token)

song_uris = []

for song in song_names:
    print(f"song_name : {song}")
    result = spotify.search(q='track:' + song, type='track')
    # out_file = open("myfile.json", "w") 
    # json.dump(result, out_file, indent = 6) 
    try:
        url = result["tracks"]["items"][0]["external_urls"]["spotify"]
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(url)
    except IndexError:
        print(f"{song} : Song not found.")


username = spotify.current_user()["id"]
print(username)
playlist = spotify.user_playlist_create(username, f"Billboard Hot 100 ({date})", public=False, collaborative=False, description=f'A collection of Billboards Hot 100 on {date}.')
spotify.user_playlist_add_tracks(username, playlist['id'], song_uris)


