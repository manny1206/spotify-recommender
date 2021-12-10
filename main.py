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

# takes the id of a playlist and returns a dictionary of track ids and track features
def retrieve_track_ids(playlist_id):
    results = spot.playlist_tracks(playlist_id)
    tracks = {}

    # loop through the first 50 songs
    for index in range(50):
        if(index >= len(results["items"])):
            break
        try:
            # stores a single track
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

# takes a string of the file name, and returns a dictionary of playlist id with a list of song ids
def parse_spreadsheet(file):
    print("parse_spreadsheet")
    spreadsheet = pd.read_csv(file)
    # sorts the playlist by the number of followers
    spreadsheet.sort_values(by="Followers")
    dataset = {}

    for index in range(100):
        # gets the uri/id of a playlist
        playlist_id = spreadsheet["URL"][index][-22:]
        # gets song id in the playlist
        dataset[playlist_id] = retrieve_track_ids(playlist_id)

        if((index + 1) % 10 == 0):
            print("{}% complete".format(index + 1))

    return dataset

# takes in a dictionary tha represents track features, and stores the desired variables into a list
def extract_track_features(features):
    my_features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                   'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']

    result_features = []

    if(features is None):
        return

    for f in my_features:
        result_features.append(features[f])

    return result_features

# takes in the data set and a song id and determines the playlist most similar to the song
def determine_similarity(dataset, user_song_id):
    print("determine_similarity")
    # gets the features of the given song
    user_track_feature = extract_track_features(spot.audio_features(user_song_id)[0])
    similarity_score = {}

    # loops though each playlist in the data set
    for playlist in dataset.keys():
        playlist_similarity = 0

        #loop through each song in the playlist
        for track in dataset[playlist].values():
            # gets the features of a song in the playlist
            track_feature = extract_track_features(track)
            # calculates how the distance/similarity of two songs features
            track_similarity = distance.euclidean(user_track_feature, track_feature)
            # stores the sum of the similarity of all songs in the playlist
            playlist_similarity += track_similarity

        # calculates the average similarity and store it with a playlist id
        similarity_score[playlist] = playlist_similarity / len(dataset[playlist])

    # sorts the dictionary by the similarity (smalles - largest)(small == most similar)
    temp = sorted(similarity_score.items(), key=lambda x: x[1])
    return temp

# takes a json/dictionary of the user's top songs and puts the song ids in a list
def parse_user_top_songs(user_song_json):
    song_list = user_song_json["items"]
    user_songs = []

    for song in song_list:
        user_songs.append(song["id"])

    return user_songs

def main():
    start = time.time()
    print("Start")

    # comment this portion out to run the code
    # with open('my_top_songs.txt') as json_file:
    #     my_top_songs = json.load(json_file)
    #
    # user_song_list = parse_user_top_songs(my_top_songs)
    # print(user_song_list)

    parse = True

    # list of songs for testing
    song_list = ["6H3TW6uEe3RxW8CcnXJfq2", "6UelLqGlWMcVH1E5c4H7lY", "6D6HVKe7Qu3imn4zzJD0W9", "7w87IxuO7BDcJ3YUqCyMTT",
                 "5qEn8c0MBzyRKgQq91Vevi", "0GO8y8jQk1PkHzS31d699N", "152lZdxL1OR0ZMW6KquMif", "22UDw8rSfLbUsaAGTXQ4Z8",
                 "77Ft1RJngppZlq59B6uP0z", "5HCyWlXZPP0y6Gqq8TgA20", "27NovPIUIRrOZoCHxABJwK", "3USxtqRwSYz57Ewm6wWRMp"]

    # parses the data from the csv, and stores it in a file 
    if(parse):
        print("Parsing data")
        dataset = parse_spreadsheet("spotify_officialplaylists.csv")
        with open('spotify_dataset', 'wb') as fp:
            pickle.dump(dataset, fp)
        fp.close()
    # loads the data set from file
    else:
        print("Retrieving Data")
        with open('spotify_dataset', 'rb') as fp:
            dataset = pickle.load(fp)

    # used to store the recommendations 
    results_file = open("results.txt", "w")

    # loop for testing, store recommendations for songs in list above
    for my_song in song_list:
        similar_playlist = determine_similarity(dataset, my_song)[0][0]
        my_playlist = spot.playlist(similar_playlist)

        # print("My song is {} by {}".format(spot.track(my_song)["name"], spot.track(my_song)["artists"][0]["name"]))
        # print("My recommended playlist is {} - {}".format(my_playlist["name"],my_playlist["external_urls"]["spotify"]))
        # print("My song is {} by {}. My recommended playlist is {} - {}".format(spot.track(my_song)["name"], spot.track(my_song)["artists"][0]["name"], my_playlist["name"],my_playlist["external_urls"]["spotify"]))
        # results_file.write("My song is {} by {}. My recommended playlist is {} - {}\n".format(spot.track(my_song)["name"], spot.track(my_song)["artists"][0]["name"], my_playlist["name"],my_playlist["external_urls"]["spotify"]))
        results_file.write("{} by {} ---> {} {}\n".format(spot.track(my_song)["name"], spot.track(my_song)["artists"][0]["name"], my_playlist["name"], my_playlist["external_urls"]["spotify"]))

    print("Done")
    print(time.time() - start)

if __name__ == '__main__':
    main()
