import spotipy
import pandas as pd
from scipy.spatial import distance
from spotipy.oauth2 import SpotifyClientCredentials

import time
import pickle
import json

id = "fc40f86251ce4a378422d00d57473fa1"
secret = "fc84316bd37244a58a4327916855496d"
# url = "http://127.0.0.1:8080/"
url = "http://localhost:3000"
my_scope = "user-library-read"
spot = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=id, client_secret=secret))


# takes the id of a playlist and returns a dictionary of track ids and track features
def retrieve_track_info(playlist_id):
    results = spot.playlist_tracks(playlist_id)
    tracks = {}

    # loop through the first 50 songs
    for index in range(50):
        if (index >= len(results["items"])):
            break
        try:
            # stores a single track
            temp_track = results["items"][index]["track"]

            if (temp_track is None):
                print("track is none type {} {}".format(index, playlist_id))

            elif (temp_track["id"] is None):
                print("track is none type {} {}".format(index, playlist_id))

            else:
                song_id = temp_track["id"]
                song_features = spot.audio_features([song_id])[0]
                if (song_features is not None):
                    artist_id = temp_track["artists"][0]["id"]
                    artist_genres = spot.artist(artist_id)["genres"]
                    tracks[song_id] = (song_features, artist_genres)

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
        dataset[playlist_id] = retrieve_track_info(playlist_id)

        if ((index + 1) % 10 == 0):
            print("{}% complete".format(index + 1))

    return dataset


def extract_track_features(track):
    track_features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                   'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']

    return {ftr: track[ftr] for ftr in track_features}


# gets the top 10 most similar songs
def recommend(dataset, user_top_songs):
    distances = {}
    user_avgs = user_top_songs_feature_avgs(user_top_songs)
    user_genres = list(dict(get_users_top_genres(spot.tracks(user_top_songs))).keys())

    # loops though each playlist in the data set
    for playlist in dataset.keys():
        for track in dataset[playlist].values():
            features = extract_track_features(track[0])
            if any(genre in user_genres for genre in track[1]):
                distances[track[0]["id"]] = distance.euclidean(list(user_avgs.values()), list(features.values()))
        
    distances = {id: distance for id, distance in sorted(distances.items(), key=lambda item: item[1])}
    recommended_ids = list(distances.keys())[:10]
    
    return spot.tracks(recommended_ids)


# takes a json/dictionary of the user's top songs and puts the song ids in a list
def parse_user_top_songs(user_song_json):
    song_list = user_song_json["items"]
    user_songs = []

    for song in song_list:
        user_songs.append(song["id"])

    return user_songs


def user_top_songs_feature_avgs(user_songs_ids):
    features_df = pd.DataFrame(spot.audio_features(user_songs_ids))

    return dict(features_df.mean())


def playlist_feature_avgs(playlist):
    features_list = []
    for track in playlist:
        features_list.append(extract_track_features(track))

    features_df = pd.DataFrame(features_list)

    return dict(features_df.mean())


def load_dataset():
    with open('spotify_dataset', 'rb') as fp:
        dataset = pickle.load(fp)

    return dataset

# takes in a dictionary/json of the user's top songs
def get_users_top_genres(song_dict):
    user_genres = {}

    # loops through each track
    for track in song_dict["tracks"]:
        artist_id = track["artists"][0]["id"]
        artist_genres = spot.artist(artist_id)["genres"]
        
        #stores each genre of the artist in a dictionary
        for genre in artist_genres:
            if(genre not in user_genres):
                user_genres[genre] = 1
            else:
                user_genres[genre] = user_genres[genre] + 1

    # user_genres = {genre: user_genres for genre, user_genres in sorted(genre.items(), key=lambda item: item[1])}

    return sorted(user_genres.items(), key=lambda x: x[1], reverse=True)[:3]

def main():
    start = time.time()
    print("Start")

    parse = True

    # parses the data from the csv, and stores it in a file
    if (parse):
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

    # file = open("my_top_songs.txt")
    # user_dict = json.load(file)
    # user_genres = get_users_top_genres(user_dict)
    # print(user_genres)

    print("Done")
    print(time.time() - start)


if __name__ == '__main__':
    main()
