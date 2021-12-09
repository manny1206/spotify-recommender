from flask import Flask, jsonify, request

app = Flask(__name__)

# request format: /recommend?user_id={user_id}&token={token}
@app.route('/recommend')
def index():
  user_id = request.args.get("user_id")
  token = request.args.get("token")
  return jsonify('Hello world')

if __name__ == '__main__':
  app.run(debug=True, host='localhost', port=3002)