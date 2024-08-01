# JSON-Translator-Microservice
CS361 - Microservice that translates the values in a JSON file to another language

# Set Up
1) Download:
microserviceA.py
(Optional) flask_test_app.py
3) Open microserviceA.py and use terminal to install following packages:
- Flask > pip install flask
- translate > pip install translate
  
# Main Program Integration
- Screenshots are from the **flask_test_app.py** which can be found in this repository.
- **Required imports in main program:**
- ![pycharm64_PyFLre0WW7](https://github.com/user-attachments/assets/aa71e47e-3a00-4a44-8342-8be7b7279843)
  
- **IMPORTANT!** If using jsonify, this is a required flask setting to ensure that special characters in other languages are written correctly:
- ![pycharm64_Nc255e17Ip](https://github.com/user-attachments/assets/7348fd01-1486-4642-b7d6-3fc958d74b24)
- Create GET route and function with preferred naming/path
- ![pycharm64_FyN3vLQ4gJ](https://github.com/user-attachments/assets/6eb5a7d3-8302-4d4b-8669-ab6c9caad487)
- Open and load data from the JSON file you want translated (using this method requires json file to be in same directory as your flask app)
- ![pycharm64_UEZWNWLF3t](https://github.com/user-attachments/assets/c2c5d453-9ab2-4771-9beb-53b3945c8079)
- Send a request to **port 5001** with path **'/process_json'**
- ![pycharm64_RJ8qCBsA1z](https://github.com/user-attachments/assets/c3c74c65-d8a2-4fd5-9ca4-3e5341c93721)
- Set a variable to hold the response with translated json data
- ![pycharm64_RnxS5VajeL](https://github.com/user-attachments/assets/9867017b-7508-4d82-84e2-37584a5a2925)
- Write the translated data to your preferred json file
- **IMPORTANT!** If using json.dump, set 'ensure_ascii=False' in the arguments or special characters may not be written correctly
- ![pycharm64_HrU8nn7jVP](https://github.com/user-attachments/assets/66edffd5-b323-4e71-ab5c-c24c06d4b7a0)
- If needed, return the translated data with jsonify
- ![pycharm64_3RVjTidLJ1](https://github.com/user-attachments/assets/c672a6d0-fa84-4b22-a1a5-c144190461ef)

# Call microservice
1) Run your flask app
2) Run the microservice
3) In a browser enter 'https://your_url.com/translate_json' or whatever path name you decided on in the route function
4) You may need to wait a few seconds for the JSON object to be returned. The translation package is somewhat slow.

# Running the flask test app program
I've included a simple flask app that will request and receive a translated JSON file
1) Download microserviceA.py, flask_test_app.py, and your_file_name.json
2) your_file_name.json must be in the same directory as flask_test_app.py
3) Download the required packages if needed:
- microserviceA.py: flask and translate
- flask_test_app.py: flask, json, and requests
4) Run flask_test_app.py
5) Run microserviceA.py
6) In your browser enter 'http://127.0.0.1:5000/translate_json'
7) Wait a few moments for the translation package to run, then the data will be displayed in the browser.










