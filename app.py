import sys

from backend.database.connection import start_connection

from backend.weather.weather_info import WeatherInfo
from backend.weather.weather_api_key import api_key

from backend.location.get_user_location import get_user_location

from PyQt5.QtWidgets import QApplication, QMainWindow
from frontend.views.login_view import Ui_LoginWindow


from backend.models.user_model import UserModel

if __name__ == "__main__":
      # lati, longi = get_user_location()
 
      # ww = WeatherInfo()
      
      # print(ww.get_temperature(api_key.get("key"), lati, longi))
      

      # app = QApplication(sys.argv)
      # mainWindow = QMainWindow()
      # ui = Ui_LoginWindow()
      # ui.setupUi(mainWindow)
      # mainWindow.show()
      # sys.exit(app.exec_())
                   
      pass
