from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*', path='/be/api/io')

app.config['SECRET_KEY'] = 'dfadfqa452rfacv1333333334532f'

CORS(app)

@app.route('/')
def index():
    i = 1
    while  i <= 10:
        show_msg('Тестируем вещание '+(str(i)))
        print(i)
        i += 1 
    return render_template('index.html')


@app.route('/test')
def test():
    i = 1
    while  i <= 10:
        show_msg('Тестируем вещание '+(str(i)))
        print(i)
        i += 1 
    return render_template('index.html')

@socketio.event
def show_msg(msg):
    print(msg)
    socketio.emit("log_message", { "text": msg})  

if __name__ == "__main__":
    socketio.run(app, host='localhost', port=5000)

