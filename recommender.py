import spotipy
import pandas as pd
from scipy.spatial import distance
from spotipy.oauth2 import SpotifyClientCredentials

import time
import pickle

id = "075c7aa80d9342b5a0773bedf7700940"
secret = "803fce8441af4f1ebef12b40c03bd0aa"
# url = "http://127.0.0.1:8080/"
url = "http://localhost:3000"
my_scope = "user-library-read"
spot = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=id, client_secret=secret))

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
def extract_track_features(track):
    track_features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                   'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']

    return {ftr: track[ftr] for ftr in track_features}

# gets the top 10 most similar songs
def recommend(dataset, user_top_songs):
    distances = {}
    user_avgs = user_top_songs_feature_avgs(user_top_songs)

    # loops though each playlist in the data set
    for playlist in dataset.keys():
        for track in dataset[playlist].values():
            features = extract_track_features(track)
            distances[track["id"]] = distance.euclidean(list(user_avgs.values()), list(features.values()))
        
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

def main():
    start = time.time()
    print("Start")

    parse = True

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

    print("Done")
    print(time.time() - start)

if __name__ == '__main__':
    main()
