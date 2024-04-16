def validar_maioridade(age):
    if age >= 18:
        return True
    else:
        return False

#idade= int(input("Digite a sua idade: "))
#if validar_maioridade(idade) == True:
    print('você é maior de idade')
#else:
#    print('Você é menor de idade')



def cadastrar(nome, sobrenome, senha):
    cadastronome= nome
    cadastrosobrenome = sobrenome
    cadastrosenha = senha
    dados = {'Nome':cadastronome,
             'Sobrenome':cadastrosobrenome,
             'Senha':cadastrosenha}
    print(f'Usuario {cadastronome} cadastrado com sucesso!')
    return dados

nome_pessoa = input('digite seu nome')
sobrenome_pessoa = input ('digite seu sobrenome')
senha_pessoa = input('digite sua senha')

cadastrar(nome_pessoa,sobrenome_pessoa,senha_pessoa)





