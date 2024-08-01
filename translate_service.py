from flask import Flask, request, jsonify
from translate import Translator

app = Flask(__name__)

@app.route('/process_json', methods=['POST'])
def process_json():
    json_data = request.get_json()


    # Set translation language
    translator = Translator(to_lang="es")

    # Loop through loaded JSON data, retrieve title and task values then translate
    for i in range(1, len(json_data) + 1):
        index = str(i)
        title_translation = translator.translate(json_data[index]['title'])
        desc_translation = translator.translate(json_data[index]['description'])
        json_data[index]['title'] = title_translation
        json_data[index]['description'] = desc_translation

    # Return modified JSON data
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
