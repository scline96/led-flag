from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
        return render_template('index.html')


@socketio.on('button')
def buttonPressed(button_name):
    print(str(button_name) + ' pressed!')

if __name__ == '__main__':
    socketio.run(app, use_reloader=False, port=5000, host='0.0.0.0', debug=True)
