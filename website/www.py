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

<<<<<<< HEAD
@socketio.on('button')
=======
## On the socketio call 'button'
@socketio.on('button', namespace='/led')
>>>>>>> 0257a393f087bb914c1e2ddd4d7edbbc61ba9e2c
def buttonPressed(button_name):
    # Print that the user pressed a button
    print(str(button_name) + ' pressed!')

<<<<<<< HEAD
=======
    '''
        This is where the LED stuff can happen, we can also add more
        socketio.on statements for different buttons or other actions 
        from the front-end.

        We can also send data to javascript using the socketio.emit()
    '''


>>>>>>> 0257a393f087bb914c1e2ddd4d7edbbc61ba9e2c
if __name__ == '__main__':
    socketio.run(app, use_reloader=False, port=5000, host='0.0.0.0', debug=True)
