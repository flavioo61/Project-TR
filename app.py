import requests
from flask import Flask, render_template

app = Flask(__name__)

# API Keys
WEATHER_API_KEY = 'b714abf37e3f2c5a74f45c00c7ff9a6c'
CITIES = [
    'Lisboa', 'Braga', 'Porto', 'Coimbra', 'Évora', 'Faro', 'Funchal', 'Ponta Delgada', 'Angra do Heroísmo', 'Horta',
    'Vila Real', 'Viseu', 'Guarda', 'Castelo Branco', 'Santarém', 'Portalegre', 'Beja', 'New York', 'London', 'Paris',
    'Tokyo', 'Sydney', 'Dubai', 'Rio de Janeiro', 'Cairo', 'Moscow', 'Cape Town', 'Bangkok', 'Seoul'
]
# Função para obter informações meteorológicas de uma cidade
def get_weather(city_name):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name, 'appid': WEATHER_API_KEY}
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp'] - 273.15  # Converter de Kelvin para Celsius
        return f"{weather_description}, {temperature:.1f}°C"
    else:
        return f"Erro ao obter informações meteorológicas: {data['message']}"

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para exibir informações sobre uma cidade específica
@app.route('/city/<city_name>')
def city_info(city_name):
    weather_info = get_weather(city_name)
    # Aqui você pode ser adicionado chamadas a outras APIs para obter informações sobre pontos turísticos,conforme for evoluindo.
    return render_template('city_info.html', city=city_name, weather_info=weather_info)

if __name__ == "__main__":
    app.run(debug=True)
