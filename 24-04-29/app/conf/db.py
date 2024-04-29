import sqlite3

db_name = 'ciencia_dados.sqlite'

cursor = sqlite3.connect(db_name).cursor()
print(cursor)