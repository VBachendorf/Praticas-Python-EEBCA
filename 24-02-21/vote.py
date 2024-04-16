def listar_candidatos():
    print('#######################')
    print("# Lista de Candidatos #")
    print('#######################')
    print('# Digite o Número de  #')
    print('#   Inscrição do      #')
    print('#    Candidato        #')
    print('#######################')
    print('# 1 - Carlinda       #')
    print('# 2 - Djeniffer      #')
    print('# 3 - Leonardo       #')
    print('# 4 - Lucila         #')
    print('#######################')

qtd_votacao = int(input("Digite a Quantidade de Votações: "))
voto_carlinda = 0
voto_djeniffer = 0
voto_leonardo = 0
voto_lucila = 0
nulo_branco = 0


for x in range(qtd_votacao):
    listar_candidatos()
    num_inscricao = input("Informe o Número de seu candidato ")
    if num_inscricao == '1':
        voto_carlinda += 1
        print('Voto computado em Carlinda')
    elif  num_inscricao == '2':
        voto_djeniffer += 1
        print('Voto computado em Djeniffer')
    elif  num_inscricao == '3':
        voto_leonardo += 1
        print('Voto computado em Leonardo')
    elif  num_inscricao == '4':
        voto_lucila += 1
        print('Voto computado em Lucila')
    else:
        nulo_branco +=1
        print('Voto computado como NULO/BRANCO')

print('\n\n ################# RESULTADOS DA VOTAÇÃO ################# \n')
print('#------------------------------------------------------------#')
print(f'# Votos para Carlinda:  |{voto_carlinda}|  -->  {voto_carlinda/qtd_votacao*100:.2f} % dos votos' )
print(f'# Votos para Djeniffer: |{voto_djeniffer}|  -->  {voto_djeniffer/qtd_votacao*100:.2f} % dos votos' )
print(f'# Votos para Leonardo:  |{voto_leonardo}|  -->  {voto_leonardo/qtd_votacao*100:.2f} % dos votos' )
print(f'# Votos para Lucila:    |{voto_lucila}|  -->  {voto_lucila/qtd_votacao*100:.2f} % dos votos' )


