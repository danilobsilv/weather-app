import sqlite3
import datetime

from backend.exceptions.userNotFound import UserNotFound
from backend.exceptions.sqliteError import SQLiteException


class UserModel:
      def __init__(self):
            self.db_path = "weather_app_db.db"

      
      def create_user(self, email, username, password):
        
            try:
         
                  connection = sqlite3.connect(self.db_path)
                  current_date = datetime.datetime.now()

                  connection.execute("""
                        INSERT INTO users (user_email, user_name, user_password, user_creation)
                        VALUES (?, ?, ?, ?)
                        """, (email, username, password, current_date))

                  connection.commit()
                  print("usuário inserido com sucesso!")


            except sqlite3.Error as error:
                  return f"ERROR --> {error}"


            except Exception as error:
                  return f"ERROR --> {error}"


            finally:
                  connection.close()
                  print("conexão fechada com sucesso!")


      def get_users(self):
            try:
                  connection = sqlite3.connect(self.db_path)

                  cursor = connection.execute("SELECT * FROM users")
                  users = cursor.fetchall()
                  return users
            
            except sqlite3.Error as error:
                  return f"ERROR --> {error}"
            
            finally:
                  connection.close()


      def get_user_by_id(self, id):
            try:
                  connection = sqlite3.connect(self.db_path)

                  cursor = connection.execute("SELECT * FROM users WHERE user_id = ?", (id,))
                  user = cursor.fetchone()

                  if user is None:
                        raise UserNotFound("usuarop num foi encontrado vivo")        
                  return user


            except sqlite3.Error as error:
                  raise SQLiteException(f" SQlite error: {error}") 

            finally:
                  connection.close()


      def get_user_by_email(self, email):
            try:
                  connection = sqlite3.connect(self.db_path)

                  cursor = connection.execute("SELECT user_email FROM users WHERE user_email = ?", (email,))
                  user = cursor.fetchone()

                  if user is None: return "User not found."
                                          
                  return user


            except sqlite3.Error as error:
                  return f"ERROR --> {error}"

            finally:
                  connection.close()


