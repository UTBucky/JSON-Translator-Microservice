from flask import Flask, request, jsonify, send_file
import json
import requests

app = Flask(__name__)
# Special characters in other languages may not display correctly without ensure_ascii set to False
app.json.ensure_ascii = False    # REQUIRED

# GET route to send JSON file to microservice then receive translated JSON object
@app.route('/translate_json', methods=['GET'])
def send_json_to_microservice():
    try:

        # Set JSON file that you want translated
        # Requires a "to_language" key with ISO 639 language code value (eg. "to_language": "es" for Spanish)
        with open('your_file_name.json', 'r') as file:
            json_data = json.load(file)

        # Set your URL with port 5001 and a path to /process_json to access microservice
        response = requests.post('http://127.0.0.1:5001/process_json', json=json_data)
        response.raise_for_status()

        # Get translated JSON from microservice
        updated_json = response.json()

        # Set the file to write the translated JSON to (ensure_ascii must be set to False for special characters)
        with open('updated_data.json', 'w') as file:
            json.dump(updated_json, file, ensure_ascii=False)

        # Uncomment below to view JSON in browser for testing
        # return jsonify(updated_json)

    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"HTTP request failed: {e}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)