lista_produtos=[]
lista_preco=[]
lista_qtd=[]

produtos_efeijao =['Arroz','Feijão','Macarrão'] 
preco_efeijao =['23.90', '14.50','3.99']
estoque_efeijao= [7,6,8] #quantidade


x=(produtos_efeijao.index('Macarrão'))
#print(produtos_efeijao[2])
print(f'Preço de produtos:') 
print('|qtd |  Produto     | Preço')   
print(f'|{estoque_efeijao[x]  } |{produtos_efeijao[x]}| {preco_efeijao[x]}')
