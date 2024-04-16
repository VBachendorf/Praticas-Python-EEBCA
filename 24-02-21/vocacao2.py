def listar_candidatos(candidatos):
    print('#######################')
    print("# Lista de Candidatos #")
    print('#######################')
    print('# Digite o Número de  #')
    print('#   Inscrição do      #')
    print('#    Candidato        #')
    print('#######################')
    
    for num, candidato in enumerate(candidatos, start=1):
        print(f'# {num} - {candidato} {" " * (18 - len(candidato))} #')
    
    print('#######################')

candidatos = ["Carlinda", "Djeniffer", "Leonardo", "Lucila"]
votos = [0] * len(candidatos)
nulo_branco = 0

qtd_votacao = int(input("Digite a Quantidade de Votações: "))

for _ in range(qtd_votacao):
    listar_candidatos(candidatos)
    num_inscricao = input("Informe o Número de seu candidato: ")
    
    if num_inscricao.isdigit() and 1 <= int(num_inscricao) <= len(candidatos):
        votos[int(num_inscricao) - 1] += 1
        print(f'Voto computado em {candidatos[int(num_inscricao) - 1]}')
    else:
        nulo_branco += 1
        print('Voto computado como NULO/BRANCO')

print('\n\n ################# RESULTADOS DA VOTAÇÃO ################# \n')
print('#------------------------------------------------------------#')

for candidato, voto in zip(candidatos, votos):
    percentual = voto / qtd_votacao * 100
    print(f'# Votos para {candidato}: {" " * (14 - len(candidato))}|{voto}|  -->  {percentual:.2f} % dos votos' )

print(f'# Votos Nulos/Brancos:   {" " * 5}|{nulo_branco}|  -->  {nulo_branco/qtd_votacao*100:.2f} % dos votos' )
