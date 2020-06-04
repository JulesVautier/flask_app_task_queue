import rq
from flask import Flask
from flask import request
from flask_api import status

from redis import Redis

from app.services.service_types import ServiceTypes
from app.worker import task_handler

app_flask = Flask(__name__)
app_flask.config['MAIL_USERNAME'] = 'julesvautier@gmail.com'
redis = Redis(host='redis', port=6379)
q = rq.Queue(connection=redis)

ENABLED_SERIVCES = [
    ServiceTypes.SLACK,
    ServiceTypes.EMAIL,
    ServiceTypes.LOG,
]

@app_flask.route('/', methods=['POST'])
def post():
    for service_type in ENABLED_SERIVCES:
        job = q.enqueue(task_handler, {'service_type': service_type, 'message': request.get_json()['message']})
    return request.get_json()['message'], status.HTTP_200_OK