from flask import Flask, request, jsonify
import the_2048
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize the game state
matrix = the_2048.start_game()

@app.route("/", methods=["GET", "POST"])
def main():
    global matrix
    
    if request.method == "POST":
        key = request.json.get("key")
        
        if key == "up":  
            the_2048.move_up(matrix)
        elif key == "down": 
            the_2048.move_down(matrix)
        elif key == "left":
            the_2048.left(matrix)
        elif key == "right": 
            the_2048.right(matrix)
        else:
            return jsonify({"error": "Invalid input"})
            
        status = the_2048.current_state(matrix)
        response = {"matrix": matrix, "status": status}
        
        if status == 'LOST':
            response["message"] = "You lost!"
            restart_game()
        elif status == 'You won!':
            response["message"] = "You won!"
            restart_game()
        else:
            the_2048.add_two(matrix)
            
        return jsonify(response)
    
    return jsonify(matrix)

@app.route("/restart", methods=["POST", "OPTIONS"])  # Allow OPTIONS requests for CORS preflight
def restart_game():
    global matrix
    matrix = the_2048.start_game()
    return jsonify(matrix)

if __name__ =='__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
