import spotipy
import pandas as pd
# import yaml
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import math
from scipy.spatial import distance

import time
import pickle
import json

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

            elif(temp_track["id"] is None):
                print("track is none type {} {}".format(index, playlist_id))

            else:
                song_id = temp_track["id"]
                song_features = spot.audio_features([song_id])[0]
                if(song_features is not None):
                    tracks[song_id] = song_features


        except spotipy.exceptions.SpotifyException:
            print("Spotipy Exception")

        except:
            print("This shit is fucking broken")

    return tracks


def parse_spreadsheet(file):
    print("parse_spreadsheet")
    spreadsheet = pd.read_csv(file)
    spreadsheet.sort_values(by="Followers")
    dataset = {}

    for index in range(100):
        playlist_id = spreadsheet["URL"][index][-22:]
        dataset[playlist_id] = retrieve_track_ids(playlist_id)

        if((index + 1) % 10):
            print("{}% complete".format(index + 1))

    return dataset

def extract_track_features(features):
    my_features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                   'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']

    result_features = []

    if(features is None):
        return

    for f in my_features:
        result_features.append(features[f])

    return result_features


def determine_similarity(dataset, user_song_id):
    print("determine_similarity")
    user_track_feature = extract_track_features(spot.audio_features(user_song_id)[0])
    similarity_score = {}

    for playlist in dataset.keys():
        playlist_similarity = 0

        for track in dataset[playlist].values():
            track_feature = extract_track_features(track)

            track_similarity = distance.euclidean(user_track_feature, track_feature)
            playlist_similarity += track_similarity

        similarity_score[playlist] = playlist_similarity / len(dataset[playlist])


    temp = sorted(similarity_score.items(), key=lambda x: x[1])
    return temp

def parse_user_top_songs(user_song_json):
    song_list = user_song_json["items"]
    user_songs = []

    for song in song_list:
        user_songs.append(song["id"])
        print(song["name"])

    return user_songs

def main():
    start = time.time()
    print("Start")

    with open('my_top_songs.txt') as json_file:
        my_top_songs = json.load(json_file)

    user_song_list = parse_user_top_songs(my_top_songs)
    print(user_song_list)

    parse = False

    song_list = ["6H3TW6uEe3RxW8CcnXJfq2", "6UelLqGlWMcVH1E5c4H7lY", "6D6HVKe7Qu3imn4zzJD0W9", "7w87IxuO7BDcJ3YUqCyMTT",
                 "5qEn8c0MBzyRKgQq91Vevi", "0GO8y8jQk1PkHzS31d699N", "152lZdxL1OR0ZMW6KquMif", "22UDw8rSfLbUsaAGTXQ4Z8",
                 "77Ft1RJngppZlq59B6uP0z"]

    if(parse):
        print("Parsing data")
        dataset = parse_spreadsheet("spotify_officialplaylists.csv")
        with open('spotify_dataset', 'wb') as fp:
            pickle.dump(dataset, fp)
        fp.close()
    else:
        print("Retrieving Data")
        with open('spotify_dataset', 'rb') as fp:
            dataset = pickle.load(fp)

    results_file = open("results.txt", "w")

    for my_song in song_list:
        similar_playlist = determine_similarity(dataset, my_song)[0][0]
        my_playlist = spot.playlist(similar_playlist)

        # print("My song is {} by {}".format(spot.track(my_song)["name"], spot.track(my_song)["artists"][0]["name"]))
        # print("My recommended playlist is {} - {}".format(my_playlist["name"],my_playlist["external_urls"]["spotify"]))
        # print("My song is {} by {}. My recommended playlist is {} - {}".format(spot.track(my_song)["name"], spot.track(my_song)["artists"][0]["name"], my_playlist["name"],my_playlist["external_urls"]["spotify"]))
        # results_file.write("My song is {} by {}. My recommended playlist is {} - {}\n".format(spot.track(my_song)["name"], spot.track(my_song)["artists"][0]["name"], my_playlist["name"],my_playlist["external_urls"]["spotify"]))
        results_file.write("{} by {} ---> {} {}\n".format(spot.track(my_song)["name"], spot.track(my_song)["artists"][0]["name"], my_playlist["name"], my_playlist["external_urls"]["spotify"]))


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
