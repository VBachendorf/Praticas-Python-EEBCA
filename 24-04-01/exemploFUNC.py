def tratar_CPF(cpf):

    if len(cpf) == 11 or len(cpf) == 14:
        if len(cpf) == 11:
            print(f'Bem vindo {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\n CFP CADASTRADO!')
            
        else:
            print(f'Bem vindo {cpf}\n CNPJ CADASTRADO!')
    else:
        print('O CPF/CNPJ DIGITADO NÃO ATENDE OS REQUISITOS MINIMOS')


user_cpf = str(input('DIGITE O CPF'))
tratar_CPF(user_cpf)