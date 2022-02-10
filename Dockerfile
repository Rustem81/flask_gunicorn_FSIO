# syntax=docker/dockerfile:1

FROM python:3.10.2-slim-buster
# install psycopg2 dependencies
#RUN apt-get update -y && apt-get -y install postgresql gcc python3-dev musl-dev redis-server


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#debug

CMD gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker  --log-file=- main:app 
#gunicorn --worker-class eventlet -w 1 main:app
#gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker  --log-file=- main:app
#gunicorn -w 1 --threads 100 main:app
#gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker  -w 1 --log-file=- main:app worker_class = 'gevent'
#gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 app:app
#uvicorn 'wsgi:run()' --reload --port 5000
#gunicorn -b 127.0.0.1:5000 -k eventlet -w 1  


