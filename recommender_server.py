import spotipy
import recommender
from flask_cors import CORS
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
CORS(app)

class Status(Resource):    
  def get(self):
    try:
      return {"data": "Api running"}
    except: 
      return {"data": "An error occured!"}
   
          
# request format: /recommend?token={token}
spotipy = spotipy
class Recommend(Resource):
  def get(self, token):
    if not token:
      return jsonify("improper or no token argument!")
    
    spot = spotipy.Spotify(auth=token)
    top_songs_json = spot.current_user_top_tracks()
    top_songs_ids = recommender.parse_user_top_songs(top_songs_json)
    dataset = recommender.load_dataset()
    recommended = recommender.recommend(dataset, top_songs_ids)
    
    res = jsonify(recommended)
    return res

api.add_resource(Status,"/")
api.add_resource(Recommend, "/recommend/<string:token>")

if __name__ == '__main__':
  app.run()