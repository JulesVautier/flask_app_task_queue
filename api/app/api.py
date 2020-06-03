import rq
from flask import Flask
from flask_restful import Api

from redis import Redis

from app.routes import simple_blueprint

app_flask = Flask(__name__)
app_flask.register_blueprint(simple_blueprint)
redis = Redis(host='redis', port=6379)
q = rq.Queue(connection=redis)