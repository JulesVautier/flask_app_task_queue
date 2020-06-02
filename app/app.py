# app.py - a minimal flask api using flask_restful
from flask import Flask, request
from flask_restful import Resource, Api
from flask_api import status

app = Flask(__name__)
api = Api(app)

@app.route('/',  methods=['POST'])
def post():
    return request.get_json()['text'], status.HTTP_200_OK

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')