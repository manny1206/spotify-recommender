import spotipy
import recommender
from flask import Flask, jsonify, request
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder="client/build", static_url_path="")
spotipy = spotipy

# request format: /recommend?token={token}
@app.route('/recommend', methods=["GET"])
@cross_origin()
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

@app.route("/")
@cross_origin()
def serve():
  return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
  app.run(debug=True, host='localhost', port=3002)