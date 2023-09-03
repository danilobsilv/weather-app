import sys
import time
import json

from PyQt5.QtWidgets import QApplication, QMainWindow

# from frontend.views.createAccountView import Ui_CreateAccount
# from frontend.views.loginView import Ui_MainWindow
# from frontend.ViewsController import ViewsController

from backend.exceptions.exceptions import ErrorException
from backend.weather.weatherInfo import WeatherInfo
from backend.weather.weatherApiKey import api_key
from backend.location.getUserLocation import get_user_location
from backend.weather.weatherInfo import WeatherInfo
from backend.models.userModel import UserModel

if __name__ == "__main__":
    
      # app = QApplication(sys.argv)
      # main_window = QMainWindow()
      # ui_main = Ui_MainWindow()
      # ui_create_account = Ui_CreateAccount()

      # ui_main.setupUi(main_window)
      # views_controller = ViewsController(ui_main, ui_create_account)

      # main_window.show()
      # sys.exit(app.exec_())                                                                                 
      pass
