import re

regex_cpf = r'\d{11}'
regex_nome = r'\w{0,60}'
regex_endereco = r'[a-zA-Z0-9 ]{5,60}, \d{1,5} - [a-zA-Z ]{5,60} - [a-zA-Z ]{5,50}/[A-Za-z]{2}'
regex_data_nascimento = r'\d{2}/\d{2}/\d{4}'

def validar_input(regex, mensagem, mensagem_erro):
    
    texto = input(mensagem)    

    if not (re.fullmatch(regex, texto)):
        print(mensagem_erro)
        validar_input(regex, mensagem, mensagem_erro)

    return texto

nome = validar_input(regex_nome, '\nDigite o Nome: ', 'O nome digitado não está no padrão aceitável')
cpf = validar_input(regex_cpf, '\nDigite o CPF: ', 'O CPF digitado é inválido. Digite apenas números')
endereco = validar_input(regex_endereco, '\nDigite o endereço: ', 'O endereço digitado não está no padrão aceitável')
data_nascimento = validar_input(regex_data_nascimento, '\nDigite o data: ', 'A data digitada deve está no padrão \'dd/MM/aaaa\' não está no padrão aceitável')

print(nome)
print(cpf)
print(endereco)
print(data_nascimento)
