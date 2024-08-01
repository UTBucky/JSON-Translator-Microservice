from flask import Flask, request, jsonify, send_file
import json
import requests

app = Flask(__name__)

@app.route('/send_json_to_microservice', methods=['GET'])
def send_json_to_microservice():
    try:
        with open('data.json', 'r') as file:
            json_data = json.load(file)

        response = requests.post('http://127.0.0.1:5001/process_json', json=json_data)
        response.raise_for_status()

        updated_json = response.json()

        # Save the updated JSON data to a file
        with open('updated_data.json', 'w') as file:
            json.dump(updated_json, file, indent=4, ensure_ascii=False)

        return jsonify(updated_json)
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