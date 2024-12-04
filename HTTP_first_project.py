
# import os
# from dotenv import load_dotenv
# import requests
# import openai

# #  error handling:
# from requests import HTTPError

# # url = 'https://api.github.com'
# # key = "<your-translator-key>" # Azure Translations
# # endpoint = "https://api.cognitive.microsofttranslator.com"
# # location = '<UPDATE_LOCATION>' # might be not needed (region)
# # path = '/translate'
# # constructed_url = endpoint + path



# def load_api_key() -> str:
#     """loads API key from .env"""
#     load_dotenv()
#     try:
#         openai.api_key = os.getenv('OPEN_API_KEY')
#     except ValueError:
#         print('API key not found')
#     return openai.api_key


# def get_response() -> None:
    
#     load_api_key()
#     header = {
#         'Authorization': f'Bearer {openai.api_key}'
#     }
#     url = "https://api.openai.com/v1/models"

#     response = requests.get(
#         url=url,
#         headers=header,
#     )

#     if response: # any status_code btw 200 and 399
#         print('Succes!')
        
#     else:
#         raise Exception(f'Something went wrong! Error: {response.status_code}')
    

#     # lub:
#     try:
#         response = requests.get(url, header)
#         response.raise_for_status

#     except HTTPError as http_err:
#         print(f'HTTP error ocurred: {http_err}')
#     except Exception as err:
#         print(f'Other error ocurred: {err}')
#     else:
#         print('Succes!')
#     # requests get a response and try to raise an error
#     # (for status code btw 400 and 600)
#     # If there is no error then it prints 'Succes!'

# get_response()




#  prognoza pogody z openweather map (get)
# API OpenWeatherMap
# flask - 
# postman - do testowania oprogramowania

# =======================================================
#  projekt od Marty: 

from flask import Flask, request, jsonify, render_template
from load_weather_api_key import load_weather_api_key
import requests

BASE_URL = 'http://api.weatherapi.com/v1/current.json'
API_KEY = load_weather_api_key()

app = Flask(__name__)

data_store = []

@app.route('/data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_data():
    if request.method == 'GET':
        print('Hello World')
        return render_template('index.html')
        # return jsonify(data_store), 200

    elif request.method == 'POST':
        new_data = request.form.get('city')
        # data_store.append(new_data)
        if new_data: 
            return jsonify({ 'status': 'success', 'message': f'Received city: {new_data}' }), 200 
        else: # Jeśli brak miasta w form-data 
            return jsonify({ 'status': 'error', 'message': 'City not provided in form-data' }), 400
        # return jsonify(new_data), 201

    elif request.method == 'PUT':
        if not data_store:
            return {"error": "Brak danych do aktualizacji"}, 404
        updated_data = request.json
        data_store[0] = updated_data  # Przykład: aktualizacja pierwszego elementu
        return jsonify(updated_data), 200

    elif request.method == 'DELETE':
        if not data_store:
            return {"error": "Brak danych do usunięcia"}, 404
        deleted_data = data_store.pop(0)
        return jsonify(deleted_data), 200



@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'pl'
    }
    response = requests.get(BASE_URL, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        return render_template('result.html', weather=weather_data)
    else:
        error_message = weather_data.get('message', 'Wystąpił błąd')
        return render_template('error.html', error=error_message)

 
if __name__ == '__main__':
    app.run(debug=True)
