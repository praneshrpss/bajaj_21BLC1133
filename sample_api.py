from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

def separate_data(data):
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    return numbers, alphabets

def find_highest_lowercase(alphabets):
    lowercase_letters = [ch for ch in alphabets if ch.islower()]
    if lowercase_letters:
        return max(lowercase_letters)
    return None

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        
        if not isinstance(data, list):
            return jsonify({"is_success": False, "message": "Invalid input format. 'data' should be a list."}), 400
        
        numbers, alphabets = separate_data(data)        
        highest_lowercase = find_highest_lowercase(alphabets)
        highest_lowercase_alphabet = [highest_lowercase] if highest_lowercase else []
        
        response = {
            "is_success": True,
            "user_id": "pranesh_s_06072003", 
            "email": "pranesh.s2021@vitstudent.ac.in",         
            "roll_number": "21BLC1133",       
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "message": "An error occurred: " + str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
