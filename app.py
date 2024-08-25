from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/bfhl', methods=['POST'])
def post_handler():
    data = request.get_json().get('data', [])
    user_id = 'john_doe_17091999'
    email = 'john@xyz.com'
    roll_number = 'ABCD123'
    
    # Convert all items to strings
    data = [str(item) for item in data]

    # Separate numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    # Determine the highest lowercase alphabet
    lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
    highest_lowercase_alphabet = []
    if lowercase_alphabets:
        highest_lowercase = max(lowercase_alphabets)
        highest_lowercase_alphabet = [highest_lowercase]

    response = {
        'is_success': True,
        'user_id': user_id,
        'email': email,
        'roll_number': roll_number,
        'numbers': numbers,
        'alphabets': alphabets,
        'highest_lowercase_alphabet': highest_lowercase_alphabet
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_handler():
    response = {
        'operation_code': 1
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
