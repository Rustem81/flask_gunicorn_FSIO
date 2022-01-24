from flask import Flask, render_template
from flask_socketio import SocketIO, emit
async_mode = None
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'dfadfqa452rfacv1333333334532f'
socketio = SocketIO(app, cors_allowed_origins='*', path='/be/api/io', async_mode = async_mode)

@app.route('/')
def index():
    i = 1
    while i <= 10:
        show_msg('Тестируем вещание '+(str(i)))
        print(i)
        i += 1 
    return render_template('index.html')

@socketio.event
def show_msg(msg):
    print(msg)
    socketio.emit("log_message", { "text": msg})  
    
if __name__ == '__main__':
    socketio.run(app)

def create_application():
    return app #socketio.run(app)
