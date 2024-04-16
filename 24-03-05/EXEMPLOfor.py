import pandas as pd

lista_produtos=['uva','maca','morango','abacate','melao']
lista_preco =[6,10,7,3.5,4]
lista_qnt = [12,8,4,9,6]
valordopedido=0
px=[]
df=pd.DataFrame({
    'Produtos': lista_produtos,
    'Preço': lista_preco, 
    'Quantidade': lista_qnt})

print(df)


for i in range(len(lista_produtos)):
    px.append(i)
    produto = lista_produtos[i]
    preco = lista_preco[i]
    quantidade = lista_qnt[i]
    valor_compra = preco * quantidade
    print(f'|{produto:^9}| {preco:^8} | {quantidade:^5} | {valor_compra:^12} |')
    valordopedido+=valor_compra
print(px)
print(f'Total do pedido --------- {valordopedido}R$')
print(f'Total de Impostos ------- {valordopedido*0.1}R$')
print(f'Total de Descontos ------ {valordopedido*0.05}R$')
print(f'Total de valor a pagar -- {valordopedido-(valordopedido*0.05)}R$')  