import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.150",
  port='3306',
  user="root",
  password="")
db_name = 'pet_db'

conexao = mydb.cursor()
conexao.execute(f"""INSERT INTO {db_name}.especies
                ( nome, mamifero, nome_familia)
                VALUES	 ('CACHORRO',1,'Canídeos'),
	 ('GATO',1,'Felídeos'),
	 ('jacaré',0,''),
	 ('Pássaro',0,''),
	 ('Cobra',0,'');
;""")
mydb.commit()

