#criar uma aplicação que faça a média de dois ou mais valores

numeros_para_media = int(input("Digite quantos números deseja calcular ")) 
soma = 0
divisor = numeros_para_media
for i in range (numeros_para_media):
    soma += int(input('Digite um número para calcular'))
x = soma/divisor
print(f'A média dos valores é {x}')
