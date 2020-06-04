import rq
from flask import Flask
from flask import request
from flask_api import status

from redis import Redis

from app.worker import task_handler

app_flask = Flask(__name__)
app_flask.config['MAIL_USERNAME'] = 'julesvautier@gmail.com'
redis = Redis(host='redis', port=6379)
q = rq.Queue(connection=redis)

@app_flask.route('/', methods=['POST'])
def post():
    WebClient()
    job = q.enqueue(task_handler, None)
    return request.get_json()['text'], status.HTTP_200_OK
