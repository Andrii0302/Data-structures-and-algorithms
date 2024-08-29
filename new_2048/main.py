from flask import Flask, render_template
from flask_socketio import SocketIO

import msvcrt
import the_2048

app = Flask(__name__)
socketio = SocketIO(app)


def initialize_game():
    return the_2048.start_game()

# Initialize the game matrix
matrix = initialize_game()

@app.route('/')
def index():
    return render_template('index.html', matrix=matrix)

@socketio.on('connect')
def handle_connect():
    global matrix
    # Reset the game matrix when a client connects
    matrix = initialize_game()
    # Emit the initial matrix to the client
    socketio.emit('update_matrix', matrix)

@socketio.on('keypress')
def handle_keypress(key):
    global matrix
    if key == 'up':
        the_2048.move_up(matrix)
    elif key == 'down':
        the_2048.move_down(matrix)
    elif key == 'left':
        the_2048.left(matrix)
    elif key == 'right':
        the_2048.right(matrix)
    status = the_2048.current_state(matrix)
    the_2048.printing(matrix)
    if status != 'Not over':
        print('YOU LOST')
    if status == 'You won!':
        print("You won!")
    else:
        the_2048.add_two(matrix)
    socketio.emit('update_matrix', matrix)

if __name__ == '__main__':
    socketio.run(app, debug=True)