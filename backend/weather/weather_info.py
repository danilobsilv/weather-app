from backend.weather.weather_api_key import weather_api_key
from location.get_user_location import get_user_location
import requests
import datetime
import time

class WeatherInfo:
    def __init__(self):
        self.key = weather_api_key.MY_KEY
        self.cache = {}

    def call_api(self, latitude, longitude):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.key}&q={latitude},{longitude}"

        response = requests.get(url)
        
        try:
            return response.json()
        
        except requests.exceptions as error:
            return (f"ERROR -->{response.status_code} {error}")


    def get_cached_response(self, latitude, longitude):
        cache_key = (latitude, longitude)
        if cache_key in self.cache:
            timestamp, data = self.cache[cache_key]
            # Verificar se a resposta foi armazenada há menos de 5 minutos p/ não precisar chamar de novo 
            if (datetime.datetime.now() - timestamp).total_seconds() < 300: 
                return data
            else:
                del self.cache[cache_key]
        return None


    def cache_response(self, latitude, longitude, data):
        cache_key = (latitude, longitude)
        self.cache[cache_key] = (datetime.datetime.now(), data)


    def get_temperature(self, latitude, longitude):
        cached_data = self.get_cached_response(latitude, longitude)
        if cached_data:
            cidade = cached_data['location']['name']
            temperatura_atual = cached_data['current']['temp_c']
        else:
            dados_climaticos = self.call_api(latitude, longitude)
            if dados_climaticos:
                cidade = dados_climaticos['location']['name']
                temperatura_atual = dados_climaticos['current']['temp_c']
                self.cache_response(latitude, longitude, dados_climaticos)
            else:
                return None, None

        return cidade, temperatura_atual


    def get_thermal_sensation(self, latitude, longitude):
        cached_data = self.get_cached_response(latitude, longitude)
        if cached_data:
            cidade = cached_data['location']['name']
            sensacao_termica = cached_data['current']['feelslike_c']
        else:
            dados_climaticos = self.call_api(latitude, longitude)
            if dados_climaticos:
                cidade = dados_climaticos['location']['name']
                sensacao_termica = dados_climaticos['current']['feelslike_c']
                self.cache_response(latitude, longitude, dados_climaticos)
            else:
                return None, None

        return cidade, sensacao_termica
    
    def teste(self):
        print("o import ta funcionando!")

    def print_chave(self):
        print(self.key)

latitude, longitude = get_user_location() 

ww = WeatherInfo()
ww.print_chave()
start = time.time()
print(ww.get_temperature(latitude, longitude))
print(ww.get_thermal_sensation(latitude, longitude))
end = time.time()
print(f"Tempo total: {end-start:.2f} segundos")  # medir tempo de resposta da api

