import time
import json

from backend.weather.weatherInfo import WeatherInfo
from backend.location.getUserLocation import get_user_location
from backend.weather.weatherApiKey import api_key

from colorama import Fore, Style

class Menu:
      def set_options(self, options:list):
            while True:
                  for index, option in enumerate(options):
                        if index == 0:
                              print(option)
                        else:
                              print(f"{index} - {option}")

                  if index + 1 == len(options) + 1:
                        index = 1

                  try:
                        option = int(input(f"{Fore.GREEN}Digite a opção que você deseja consultar: {Style.RESET_ALL}"))

                        if option == 1:
                              self.get_temperature()

                        elif option == 2:
                              self.get_thermal_sensation()

                        elif option == 0:
                              print(f"{Fore.LIGHTCYAN_EX}Obrigado Isa. Você é linda!")
                              time.sleep(3)
                              break

                  except ValueError:
                        print(f"{Fore.RED}Insira uma opção válida!{Style.RESET_ALL}")
                        continue 
                  

      def get_temperature(self):
            temp = WeatherInfo()
            lati, longi = self.get_location()
            temperature_data = json.loads(temp.get_temperature(api_key.get("key"), lati, longi))
            temperatura_atual = temperature_data.get('temperatura_atual', 'Temperatura não disponível')
            print(f"\n{Fore.MAGENTA}Temperatura atual: {temperatura_atual}°C\n\n")

      def get_location(self):
            lati, longi = get_user_location()
            return lati, longi
      
      def get_thermal_sensation(self):
            temp = WeatherInfo()
            lati, longi = self.get_location()
            sensation_data = json.loads(temp.get_thermal_sensation(api_key.get("key"), lati, longi))
            sensacao_termica = sensation_data.get('sensacao_termica', 'Sensação térmica não disponível')
            print(f"\n{Fore.MAGENTA}Sensação térmica atual: {sensacao_termica}°C\n\n")





menu = Menu()
menu.set_options([f"{Fore.YELLOW}Você está na cidade de Manaus. Essas são suas opções:\n", "Temperatura", "Sensação térmica ", "Clique no 0 (Zero) caso queira sair!"])
