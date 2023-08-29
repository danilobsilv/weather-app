import json
import requests
import datetime


class WeatherInfo:
    def __init__(self):
        self.cache = {}


    def call_api(self, key, latitude, longitude):
        url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={latitude},{longitude}"

        response = requests.get(url)
        
        try:
            return response.json()
        
        except requests.exceptions as error:
            return (f"ERROR -->{response.status_code} {error}")


    def get_cached_response(self, latitude, longitude):
        cache_key = (latitude, longitude)
        if cache_key in self.cache:
            timestamp, data = self.cache[cache_key]
            #Check if the answer was stored less than 5 minutes ago so you don't have to call again
            if (datetime.datetime.now() - timestamp).total_seconds() < 300: 
                return data
            else:
                del self.cache[cache_key]
        return None


    def cache_response(self, latitude, longitude, data):
        cache_key = (latitude, longitude)
        self.cache[cache_key] = (datetime.datetime.now(), data)


    def get_temperature(self, key, latitude, longitude):
        cached_data = self.get_cached_response(latitude, longitude)
        if cached_data:
            cidade = cached_data['location']['name']
            temperatura_atual = cached_data['current']['temp_c']
        else:
            dados_climaticos = self.call_api(key, latitude, longitude)
            if dados_climaticos:
                cidade = dados_climaticos['location']['name']
                temperatura_atual = dados_climaticos['current']['temp_c']
                self.cache_response(latitude, longitude, dados_climaticos)
            else:
                return json.dumps({"error": "Erro ao obter dados do clima."})

        return json.dumps({"cidade": cidade, "temperatura_atual": temperatura_atual})


    def get_thermal_sensation(self, key, latitude, longitude):
        cached_data = self.get_cached_response(latitude, longitude)
        if cached_data:
            cidade = cached_data['location']['name']
            sensacao_termica = cached_data['current']['feelslike_c']
        else:
            dados_climaticos = self.call_api(key, latitude, longitude)
            if dados_climaticos:
                cidade = dados_climaticos['location']['name']
                sensacao_termica = dados_climaticos['current']['feelslike_c']
                self.cache_response(latitude, longitude, dados_climaticos)
            else:
                return json.dumps({"error": "Erro ao obter dados do clima."})

        return json.dumps({"cidade": cidade, "sensacao_termica": sensacao_termica})
