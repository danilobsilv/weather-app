import sys

from backend.exceptions.userNotFound import UserNotFound

from backend.weather.weatherInfo import WeatherInfo
from backend.weather.weatherApiKey import api_key

from backend.location.getUserLocation import get_user_location

from PyQt5.QtWidgets import QApplication, QMainWindow
from frontend.views.loginView import Ui_MainWindow


from backend.models.userModel import UserModel

if __name__ == "__main__":
      # lati, longi = get_user_location()
 
      # ww = WeatherInfo()
      
      # print(ww.get_temperature(api_key.get("key"), lati, longi))
      

      app = QApplication(sys.argv)
      mainWindow = QMainWindow()
      ui = Ui_MainWindow()
      ui.setupUi(mainWindow)
      mainWindow.show()
      sys.exit(app.exec_())
                   
      # pass

      # from backend.controllers.user_controller import UserController 
      # user = UserController()
      # print(user.checkUserEmail("danilobsilv@gmail.com"))


      # cont = UserModel()
      # (cont.get_user_by_id("sksks"))                                                                                                                      