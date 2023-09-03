import sqlite3
import datetime

from backend.exceptions.exceptions import ErrorException

class UserModel:
      def __init__(self):
            self.db_path = "weather_app_db.db"

      def _execute_query(self, query, params=None):
            try:
                  with sqlite3.connect(self.db_path) as connection:
                        if params is None:
                              cursor = connection.execute(query)
                        else:
                              cursor = connection.execute(query, params)
                        return cursor.fetchall()

            except sqlite3.IntegrityError as error:
                  raise ErrorException(f"DataBase Integrity ERROR: {error}")

            except sqlite3.OperationalError as error:
                  raise ErrorException(f"DataBase Connection ERROR: {error}")

            except sqlite3.DatabaseError as error:
                  raise ErrorException(f"DataBase ERROR: {error}")

            except sqlite3.Error as error:
                  raise ErrorException(f"SQLite Query ERROR: {error}")

            except Exception as error:
                  raise ErrorException(f"Error: {error}")

      def create_user(self, email, username, password):
                  current_date = datetime.datetime.now()
                  query = """
                        INSERT INTO users (user_email, user_name, user_password, user_creation)
                        VALUES (?, ?, ?, ?)
                        """
                  self._execute_query(query, (email, username, password, current_date))

      def get_users(self):
            query = "SELECT * FROM users"
            return self._execute_query(query)
      
      def get_user_by_id(self, id):
            query = "SELECT * FROM users WHERE user_id = ?"
            result = self._execute_query(query, (id,))

            if not result:
                  raise ErrorException(f"User with ID {id} was not found.")
            return result[0]
      
      def get_user_by_email(self, email):
        query = "SELECT user_email FROM users WHERE user_email = ?"
        result = self._execute_query(query, (email,))
        if not result:
            raise Exception(f"User with email {email} not found.")
        return result[0][0]