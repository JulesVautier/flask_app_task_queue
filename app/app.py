# app.py - a minimal flask api using flask_restful
import rq
from flask import Flask, request
from flask_restful import Resource, Api
from flask_api import status

from app.worker import task_handler
from redis import Redis

app = Flask(__name__)
api = Api(app)
redis = Redis(host='redis', port=6379)
q = rq.Queue(connection=redis)

@app.route('/',  methods=['POST'])
def post():
    job = q.enqueue(task_handler, None)
    app.logger.info(job.get_status())
    app.logger.info(job.started_at)
    app.logger.info(q.count)
    return request.get_json()['text'], status.HTTP_200_OK

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')