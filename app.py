from flask import Flask, request, jsonify

app = Flask(__name__)

FULL_NAME = "john_doe"
DOB = "17091999"  # ddmmyyyy
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        data = request.get_json()

        if "data" not in data:
            return jsonify({"is_success": False, "message": "Missing 'data' field"}), 400

        input_data = data["data"]

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        concat_chars = []

        for item in input_data:
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                total_sum += num
            elif item.isalpha():
                alphabets.append(item.upper())
                concat_chars.append(item)
            else:
                special_characters.append(item)

        concat_string = ""
        concat_chars = "".join(concat_chars)[::-1]  # reverse string
        for i, ch in enumerate(concat_chars):
            concat_string += ch.upper() if i % 2 == 0 else ch.lower()

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500


@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1}), 200


if __name__ == '__main__':
    app.run(debug=True)
