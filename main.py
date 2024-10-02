from flask import Flask, Response
from helpers.response import response_helper

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index() -> Response:
   return response_helper('Halo :v')
  
@app.route('/user/<username>', methods=['GET'])
def user(username) -> Response:
  return response_helper(f'Halo {username}', code=500)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=1231, debug=True)