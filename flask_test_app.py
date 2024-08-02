from flask import Flask, jsonify
import json
import requests

app = Flask(__name__)
# Special characters in other languages may not display correctly without ensure_ascii set to False
app.json.ensure_ascii = False    # REQUIRED

# GET route to send JSON file to microservice then receive translated JSON object
@app.route('/translate_json', methods=['GET'])
def translate_json():
    try:
        # Set JSON file to be translated
        with open('your_file_name.json', 'r') as file:
            json_data = json.load(file)

        # Send request to translation microservice with JSON data
        # Set your URL with path to /process_json
        response = requests.post('http://your_url:5001/process_json', json=json_data)
        response.raise_for_status()

        # Get response from microservice with translated JSON
        updated_json = response.json()

        # Save the translated JSON data to a file
        # Set the file name for where you want the translated data written to
        with open('translated_data.json', 'w') as file:
            json.dump(updated_json, file, ensure_ascii=False)  # ensure_ascii required to be set to False

        # Returns json data to be displayed in browser
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