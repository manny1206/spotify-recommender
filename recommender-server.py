import re
import spotipy
from flask import Flask, jsonify, request

app = Flask(__name__)

spotipy = spotipy

# request format: /recommend?user_id={user_id}&token={token}
@app.route('/recommend', methods=["GET"])
def recommend():
  token = request.args.get("token")
  spot = spotipy.Spotify(auth=token)
  
  res = jsonify(spot.current_user_top_tracks())
  res.headers.add('Access-Control-Allow-Origin', '*')
  return res

if __name__ == '__main__':
  app.run(debug=True, host='localhost', port=3002)