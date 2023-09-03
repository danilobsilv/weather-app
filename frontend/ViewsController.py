# from PyQt5.QtWidgets import QMainWindow
# from frontend.views.loginView import Ui_MainWindow
# from frontend.views.createAccountView import Ui_CreateAccount

# class ViewsController:
#     def __init__(self):
#         self.login_window = None
#         self.create_account_window = None

#     def showLoginWindow(self):
#         if self.login_window is None:
#             self.login_window = QMainWindow()
#             self.ui_login = Ui_MainWindow()
#             self.ui_login.setupUi(self.login_window, self)

#         self.login_window.show()

#     def showCreateAccountWindow(self):
#         if self.create_account_window is None:
#             self.create_account_window = QMainWindow()
#             self.ui_create_account = Ui_CreateAccount()
#             self.ui_create_account.setupUi(self.create_account_window, self)

#         self.create_account_window.show()