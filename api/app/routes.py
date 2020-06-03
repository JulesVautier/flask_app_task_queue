from flask import request, Blueprint
from flask_api import status

from app.worker import task_handler

simple_blueprint = Blueprint('simple_page', __name__)

def simple_task(args):
    print(args)
    return args

@simple_blueprint.route('/', methods=['POST'])
def post():
    from app.api import q
    job = q.enqueue(task_handler, None)
    # simple_blueprint.logger.info(job.get_status())
    # simple_blueprint.logger.info(job.started_at)
    # simple_blueprint.logger.info(q.count)
    return request.get_json()['text'], status.HTTP_200_OK
