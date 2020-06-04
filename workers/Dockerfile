FROM python:3

WORKDIR api

COPY * /api/

# Install Python dependencies
RUN pip install rq
RUN pip install supervisor
RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/api/:/api/app/"

# Spawn workers according to config
ENTRYPOINT ["/bin/bash", "-c", "supervisord -c /usr/src/workers/supervisord.conf -n"]
