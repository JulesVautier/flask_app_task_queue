FROM python:3.7

EXPOSE 5000

WORKDIR api

COPY * /api/

RUN pip install -r requirements.txt

CMD python run.py