import spotipy
import pandas as pd
# import yaml
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

import time
import pickle

id = "075c7aa80d9342b5a0773bedf7700940"
secret = "803fce8441af4f1ebef12b40c03bd0aa"
# url = "http://127.0.0.1:8080/"
url = "http://localhost:3000"
my_scope = "user-library-read"
spot = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=id, client_secret=secret))
# spot = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=id, client_secret=secret, scope=my_scope, redirect_uri=url))
# auth_manager = SpotifyClientCredentials
# spot = spotipy.Spotify(auth_manager=auth_manager)

def retrieve_track_ids(playlist_id):
    results = spot.playlist_tracks(playlist_id)
    tracks = {}

    for index in range(50):
        if(index >= len(results["items"])):
            break
        try:
            temp_track = results["items"][index]["track"]

            if(temp_track is None):
                print("track is none type {} {}".format(index, playlist_id))

            else:
                if(temp_track["id"] is not None):
                    song_id = temp_track["id"]
                    song_name = temp_track["name"]
                    song_artist = temp_track["artists"][0]["name"]
                    tracks[song_id] = (song_name, song_artist, spot.audio_features([song_id])[0])

                else:
                    print("track id is none type {} {}".format(index, playlist_id))

        except spotipy.exceptions.SpotifyException:
            print("Spotipy Exception")

        except:
            print("This shit is fucking broken")

    return tracks


def parse_spreadsheet(file):
    spreadsheet = pd.read_csv(file)
    spreadsheet.sort_values(by="Followers")
    dataset = {}

    # for temp in spreadsheet["Description"]:
    #     print(temp)
    for index in range(100):
        playlist_id = spreadsheet["URL"][index][-22:]
        dataset[playlist_id] = retrieve_track_ids(playlist_id)

    return dataset

def determine_similarity(dataset, user_song_id):
    similarity_score = []
    temp = dataset.values()
    for playlist in dataset.values():
        for track in playlist.values():
            print("hi")
            track_feature = track[2]
            # user_track_feature =

def main():
    start = time.time()
    print("Start")

    parse = False

    if(parse):
        dataset = parse_spreadsheet("spotify_officialplaylists.csv")
        with open('spotify_dataset', 'wb') as fp:
            pickle.dump(dataset, fp)
        fp.close()
    else:
        with open('spotify_dataset', 'rb') as fp:
            dataset = pickle.load(fp)

    temp = determine_similarity(dataset, "hi")

    # print(temp)

    ###############
    # with open("spotify/spotify_details.yml", 'r') as stream:
    #     spotify_details = yaml.safe_load(stream)

    # https://developer.spotify.com/web-api/using-scopes/
    # scope = "user-library-read user-follow-read user-top-read playlist-read-private"
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    #     client_id=spotify_details['075c7aa80d9342b5a0773bedf7700940'],
    #     client_secret=spotify_details['803fce8441af4f1ebef12b40c03bd0aa'],
    #     redirect_uri=spotify_details['http://127.0.0.1:8080/'],
    #     scope=scope, )
    # )
    # temp = sp.albums()

    # print(temp)
    ########################
    # import tekore as tk
    #
    # client_id = 'your_id_here'
    # client_secret = 'your_secret_here'
    #
    # app_token = tk.request_client_token(id, secret)
    #
    # auth = SpotifyOAuth(client_id=id, client_secret=secret, redirect_uri=url)
    # sp = spotipy.Spotify(auth_manager=auth)
    # playlist = sp.current_user_playlists()
    # # playlist_url = playlist["items"][0]["external_urls"]
    # # print(playlist_url)
    #
    # spotify = tk.Spotify(app_token)
    #
    #
    # album = spotify.album('37i9dQZF1DX0XUsuxWHRQd')
    # for track in album.tracks.items:
    #     print(track.track_number, track.name)

    ###################
    # import spotipy
    #
    # urn = '3jOstUTkEu2JkjvRdBA5Gu'
    # sp = spotipy.Spotify()
    #
    # artist = sp.artist(urn)
    # print(artist)
    #
    # user = sp.user('plamere')
    # print(user)

    ######

    # birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'


    # albums = results['items']
    # while results['next']:
    #     results = spotify.next(results)
    #     albums.extend(results['items'])
    #
    # for album in albums:
    #     print(album['name'])


    print("Done")
    print(time.time() - start)

if __name__ == '__main__':
    main()
