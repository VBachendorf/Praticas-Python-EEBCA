print('---------SISTEMA 1.0---------')

lista_produtos = []
lista_preco = []
lista_qnt = []


    

while True:
    res_usuario=input("Digite 'SAIR' para encerar o programa")
    if res_usuario == "SAIR":
        print('EMISSÃO DE CUPOM FISCAL')
        print('-----------------------')
        print(f'| Produto| |Preço R$| | Qtd | | Total R$|')
        valordopedido=0
        for i in range(len(lista_produtos)):
            produto = lista_produtos[i]
            preco = lista_preco[i]
            quantidade = lista_qnt[i]
            valor_compra = preco * quantidade
            print(f'|{produto:^9}| {valor_compra:^8} | {quantidade:^5} | {valor_compra:^12} ')
            valordopedido+=valor_compra
        print(f'Total do pedido --------- {valordopedido}R$')
        print(f'Total de Impostos ------- {valordopedido*0.1}R$')
        print(f'Total de Descontos ------ {valordopedido*0.05}R$')
        print(f'Total de valor a pagar -- {valordopedido-(valordopedido*0.05)}R$')
        break
    else:
        produto = input("Nome do Produto: ")
        lista_produtos.append(produto)
        
        preco = int(input("Preço do Produto: "))
        lista_preco.append(preco)
        
        qtd = int(input("Quantidade do Produto: "))
        lista_qnt.append(qtd)