#' - 1 -- instalar  o pacote
#pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", 
  user="yourusername", 
  password="yourpassword" 
)

cursor = mydb.cursor()
try:
  cursor.execute("CREATE DATABASE IF NOT EXISTS NomeDoBancoDeDados")
  print("Database created successfully")
except mysql.connector.Error as error :
  print("Failed to create database {}".format(error))

# Fechar conexão com o banco de dados
cursor.close()
mydb.close()