lista_frutas =['maca','pera','banana', 'uva', 'manga']

lista_preco =['1.50','2.30','1.80','4.90', '3.70']
numero_frutas = len(lista_frutas)

for x in range(numero_frutas):
    print(f'Preço da fruta {lista_frutas[x]}: R$ {lista_preco[x]}')