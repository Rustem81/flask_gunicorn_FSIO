# syntax=docker/dockerfile:1

FROM python:3.8.3-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#debug

CMD gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker  --log-file=- main:app worker_class = 'gevent'

#uvicorn 'wsgi:run()' --reload --port 5000
#gunicorn -b 127.0.0.1:5000 -k eventlet -w 1  


