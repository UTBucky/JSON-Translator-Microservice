from flask import Flask, request, jsonify
from translate import Translator

app = Flask(__name__)
app.json.ensure_ascii = False

@app.route('/process_json', methods=['POST'])
def process_json():
    try:
        # Receive request with JSON data to be translated
        tasks = request.get_json()
        
        # Pulls ISO 639 code from "to_language" key to set translation language
        language = json_data.get("to_language")
        if not language:
            return jsonify({"error": "Language code is missing"}), 400
        
        # Set translation language
        translator = Translator(language)

        # Loop through loaded JSON data, retrieve title and task values, translate then replace values
        for i in range(1, len(json_data)):
            index = str(i)
            task = tasks.get(index, {})
            title = task.get('title', '')
            description = task.get('description', '')
            
            if title:
                task['title'] = translator.translate(title)
            if description:
                task['description'] = translator.translate(description)

        # Return modified JSON data
        return jsonify(json_data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
