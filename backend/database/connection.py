import mysql.connector
from db_keys import database_keys

def database_connect():
      connection = None
      try:
            connection = mysql.connector.connect(
                  host = database_keys.get("host"),
                  user = database_keys.get("user"),
                  password = database_keys.get("password"),
                  database = database_keys.get("database")
            )
            if connection.is_connected():
                  print("Conectado ao banco de dados com sucesso!")

      except mysql.connector.Error as db_conn_error:
            print(f"Erro ao conectar-se ao banco de dados --> {db_conn_error}")

      finally:
            if connection and connection.is_connected():
                  connection.close()
                  print("Conexão ao MySQL fechada!")

database_connect()