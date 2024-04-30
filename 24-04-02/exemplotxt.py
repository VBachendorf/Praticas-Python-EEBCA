import pandas as pd
def adicionar_item_arquivo( item, quantidade, preco_unitario):
    with open('file.txt', 'a') as arquivo:
        arquivo.write(f"{item}|{quantidade}|{preco_unitario}\n")

def ler_itens_arquivo():
    itens = {
        "Produto": [],
        "Quantidade": [],
        "Preço Unitário": []
    }
    with open('file.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split('|')
            item = partes[0]
            quantidade = float(partes[1])
            preco_unitario = float(partes[2])
           
            itens["Produto"].append(item)
            itens["Quantidade"].append(quantidade)
            itens["Preço Unitário"].append(preco_unitario)
    df = pd.DataFrame(itens)
    
    return df

