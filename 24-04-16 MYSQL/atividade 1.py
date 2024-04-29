#' - 1 -- instalar  o pacote
#pip install mysql-connector-python

import mysql.connector


##  Conexão com o banco de dados
mydb = mysql.connector.connect(
  host="localhost", #ip de destino seja no teu pc ou em outro lugar
  user="yourusername", #o nome de usuário do teu db
  password="yourpassword" # a senha óbvio
)
print(mydb)
# se der erro aqui eu desconto 3 pontos da média em cada ocorrência
