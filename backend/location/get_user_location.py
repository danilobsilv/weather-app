import geocoder
from weather.weather_api_key import my_key
from weather.weather_info import WeatherInfo

def get_user_location():
    g = geocoder.ip('me')
    return g.latlng  # Retorna uma tupla com latitude e longitude


# latitude, longitude = obter_localizacao_usuario()
# print(f"Latitude: {latitude}, Longitude: {longitude}")