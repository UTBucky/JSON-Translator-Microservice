from flask import Flask, request, jsonify
from translate import Translator
import json


app = Flask(__name__)
# Special characters in other languages will not display correctly without this set to False
app.json.ensure_ascii = False    # REQUIRED

@app.route('/process_json', methods=['POST'])
def process_json():
    # Receive request with JSON data to be translated
    json_data = request.get_json()

    # Pulls ISO 639 code from "to_language" key to set translation language
    language = json_data["to_language"]

    # Set translation language
    translator = Translator(language)

    # Loop through loaded JSON data, retrieve title and task values, translate then replaces values
    for i in range(1, len(json_data)):
        index = str(i)
        title_translation = translator.translate(json_data[index]['title'])
        desc_translation = translator.translate(json_data[index]['description'])
        json_data[index]['title'] = title_translation
        json_data[index]['description'] = desc_translation

    # Return modified JSON data
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(port=5001, debug=True)