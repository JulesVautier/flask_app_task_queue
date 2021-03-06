# Flask Redis Queue with docker-compose environment

Example of how to handle background processes with Flask, Redis Queue, and Docker
(inspired from [mjhea0](https://github.com/mjhea0/flask-redis-queue))

### Services

There's three implemented [services](./api/app/services):
- [Slack](./api/app/services/slack_service.py)
- [Gmail](./api/app/services/email_service.py)
- [Log](./api/app/services/log_service.py) (this is just a print ^^)

You can add/removes services by modifying the ENABLED_SERIVCES variable in [./api/app/api.py](./api/app/api.py)

### Quick Start

1 Make sure to complete the [./api/.env](./api/.env) file with correct infos

```sh
SENDER_MAIL_USERNAME=xxxxx
EMAIL_USER=xxxx
EMAIL_PASSWORD=xxxx
SLACK_API_TOKEN=xxxx
```

2 Spin up the containers:

```sh
$ docker-compose up -d --build
```

3 Send a request to the api
```shell script
curl localhost:5000 --header "Content-Type: application/json" \
  --request POST \
  --data '{"message":"HelloWorld"}'

```
### Tests
```docker-compose run --rm flask pytest app/tests/tests.py```

### How to improve ?

1. Use a schema to verify the post request's data
2. Write some RQ tests. Check if the jobs are created correctly.
3. Create a connection manager to get a real or a test connection with Redis by checking the TESTING flag instead of having a 'if' in the view
4. Handling failed jobs


### Monitoring the Redis Queue
You can access the [rq-dashboard](http://localhost:9181/) to see pending or failed jobs.