import spotipy
import recommender
from flask import Flask, jsonify, request

app = Flask(__name__)
spotipy = spotipy

# request format: /recommend?token={token}
@app.route('/recommend', methods=["GET"])
def recommend():
  token = request.args.get("token")
  if not token:
    return jsonify("improper or no token argument!")
  
  spot = spotipy.Spotify(auth=token)
  top_songs_json = spot.current_user_top_tracks()
  top_songs_ids = recommender.parse_user_top_songs(top_songs_json)
  dataset = recommender.load_dataset()
  recommended = recommender.recommend(dataset, top_songs_ids)
  
  res = jsonify(recommended)
  res.headers.add('Access-Control-Allow-Origin', '*')
  return res

if __name__ == '__main__':
  app.run(debug=True, host='localhost', port=3002)