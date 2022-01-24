# Prod 
```
 docker-compose -f docker-compose.yml up 
```
# Dev  
```
 # pip3 freeze > requirements.txt  # Python3

 venv\scripts\activate
 pip install -r requirements.txt

 $env:FLASK_APP = "app"
 flask run

 cd web/client
 npm install 
 npm run serve
``` 
# Примеры 
```
 https://github.com/miguelgrinberg/Flask-SocketIO/issues/457
 https://github.com/miguelgrinberg/Flask-SocketIO/issues/279
 https://github.com/miguelgrinberg/flack/blob/master/manage.py 
```
# off-top 
```
 docker build --tag flask_gunicorn_app .
 docker run --detach -p 80:8000 flask_gunicorn_app
```






