# app.py - a minimal flask api using flask_restful
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/',  methods=['POST'])
def index():
    if request.method == 'POST':
        return request.get_json()['text']
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')