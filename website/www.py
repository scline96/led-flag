from flask import Flask, render_template
from flask_socketio import SocketIO, emit


## Setup the flask application and socketio object
app = Flask(__name__)
socketio = SocketIO(app)


## When the user navigates to the '/' base URL
@app.route('/')
def home():
    # Return the index page
    return render_template('index.html')

@socketio.on('button')
def buttonPressed(button_name):
    # Print that the user pressed a button
    print(str(button_name) + ' pressed!')

    '''
        This is where the LED stuff can happen, we can also add more
        socketio.on statements for different buttons or other actions 
        from the front-end.

        We can also send data to javascript using the socketio.emit()
    '''


if __name__ == '__main__':
    socketio.run(app, use_reloader=False, port=5000, host='0.0.0.0', debug=True)
