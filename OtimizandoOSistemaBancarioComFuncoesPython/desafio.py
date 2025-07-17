import re

MAX_SAQUES = 3
LIMITE_SAQUE = 500.00

ACOES = [1,2,3,4]
OPERACOES = [1,2,3,4]

lista_usuarios = []
lista_contas = []

TEXTO_ACOES = '''
---------------------------------------
Escolha uma das opções:

-1: Cadastrar usuário
-2: Abrir uma conta
-3: Realizar operações em uma conta

-4: Sair/Finalizar

> '''

TEXTO_QUAL_OPERACAO = '''
---------------------------------------
Qual operação deseja realizar?
'''

TEXTO_OUTRA_OPERACAO = '''
---------------------------------------
Realizar outra operacao?
'''

TEXTO_OPCOES_OPERACAO = '''
-1 : Depósito
-2 : Saque
-3 : Ver o Extrato

-4: Sair/Finalizar

> '''

TEXTO_DEPOSITO = '''
---------------------------------------
Qual valor deseja depositar?
Pressione 'C' para cancelar

> '''

TEXTO_SAQUE = '''
---------------------------------------
Qual valor deseja sacar?
Pressione 'C' para cancelar

> '''

regex_cpf = r'\d{11}'
regex_nome = r'[a-zA-ZÀ-ÿ ]{0,60}'
regex_endereco = r'[a-zA-ZÀ-ÿ0-9 ]{5,60}, \d{1,5} - [a-zA-ZÀ-ÿ ]{5,60} - [a-zA-ZÀ-ÿ ]{5,50}/[A-Za-zÀ-ÿ ]{2}'
regex_data_nascimento = r'\d{2}/\d{2}/\d{4}'

def realizar_deposito(saldo, extrato, mensagem = ''):

    if mensagem != '':
        print(mensagem)
    resposta = input(TEXTO_DEPOSITO)

    if resposta.upper() != 'C':
        try:
            valor_deposito = float(resposta)
            saldo += valor_deposito
            extrato = f'{extrato}\n-------------------------------\nDepósito no valor de R$ {valor_deposito:.2f}'
        except:
            mensagem = f'\n---------------------------------------\nDigite o valor desejado ou pressione \'C\' para cancelar!\n'
            realizar_deposito(saldo, extrato, mensagem)

    return saldo, extrato
    
def realizar_saque(*, mensagem, saldo, saques, extrato):

    if saques != 3:
    
        if mensagem != '':
            print(mensagem)
        resposta = input(TEXTO_SAQUE)

        if resposta.upper() != 'C':
            try:
                valor_saque = float(resposta)
                if (valor_saque > 1500):
                    mensagem = f'\n---------------------------------------\nValor do saque maior que o limite permitido!\n'
                    realizar_saque(mensagem=mensagem, saldo=saldo, saques=saques, extrato=extrato)
                elif valor_saque > saldo:
                    mensagem = f'\n---------------------------------------\nSaldo insuficiente!\n'
                    realizar_saque(mensagem=mensagem, saldo=saldo, saques=saques, extrato=extrato)
                else:
                    saldo -= valor_saque
                    saques += 1
                    extrato = f'{extrato}\n-------------------------------\nSaque no valor de R$ {valor_saque:.2f}'
            except:
                mensagem = f'\n---------------------------------------\nDigite o valor desejado ou pressione \'C\' para cancelar!\n'
                realizar_saque(mensagem=mensagem, saldo=saldo, saques=saques, extrato=extrato)
    else:
        print(f'\n---------------------------------------\nO limite diário da quantidade de saques já foi atingido!\n')

    return saldo, saques, extrato

def visualizar_extrato(saldo, *, extrato):

    print(f'\nEXTRATO:\n{extrato}\n\nSaldo: R$ {saldo:.2f}')
          

def definir_operacao(pergunta, lista_contas, conta):
        
    while True:

        if lista_contas:

            saldo = conta['saldo']
            extrato = conta['extrato']
            saques = conta['saques']
            numero = conta['numero']
            index_conta = next(i for i, conta in enumerate(lista_contas) if conta['numero'] == numero)

            try:
                tipo_operacao = int(input(f'{pergunta}{TEXTO_OPCOES_OPERACAO}'))
            except:
                print('\nDigite apenas uma das opções do menu!\n')
                definir_operacao(pergunta, lista_contas, conta)
            
            if tipo_operacao not in OPERACOES:
                print('\nDigite apenas uma das opções do menu!\n')
                definir_operacao(pergunta, lista_contas, conta)
            
            if tipo_operacao == 1:
                saldo, extrato = realizar_deposito(saldo, extrato)
                conta.update({"saldo": saldo})
                conta.update({"extrato": extrato})
            elif tipo_operacao == 2:
                saldo, saques, extrato = realizar_saque(mensagem='', saldo=saldo, saques=saques, extrato=extrato)
                conta.update({"saldo": saldo})
                conta.update({"extrato": extrato})
                conta.update({"saques": saques})
                definir_operacao(TEXTO_OUTRA_OPERACAO, lista_contas, conta)
            elif tipo_operacao == 3:
                visualizar_extrato(saldo, extrato=extrato)
                definir_operacao(TEXTO_OUTRA_OPERACAO, lista_contas, conta)
            else:
                if tipo_operacao != 4:
                    definir_operacao(TEXTO_OUTRA_OPERACAO, lista_contas, conta)
                
                lista_contas[index_conta] = conta
                return lista_contas
        else:
            print('\n!!! Cadastre uma conta antes de realizar outras operações !!!\n')

            return None
        

def validar_input(regex, mensagem, mensagem_erro):
    
    while True:
        texto = input(mensagem).strip()

        if texto.capitalize == 'C':
            return texto
        
        if re.fullmatch(regex, texto):
            return texto
        print(mensagem_erro)


def verificar_usuario_existente(lista_usuarios):
    
    while True:
        
        cpf = validar_input(regex_cpf
                            ,'\nDigite o CPF ou "C" para cancelar: '
                            ,'!!! O CPF digitado é inválido. Digite exatamente 11 números !!!')
    
        for usuario in lista_usuarios:
            if cpf != usuario['cpf']:
                continue

            print('\n!!! Já existe um usuário cadastrado com este CPF !!!\n')    
            cpf = None    
        
        if cpf != None:
            return cpf


def criar_usuario(lista_usuarios):

    while True:
        
        nome = validar_input(regex_nome
                            ,'\nDigite o Nome ou "C" para cancelar: '
                            ,'O nome digitado não está no padrão aceitável (2-60 caracteres alfabéticos)')
        
        cpf = verificar_usuario_existente(lista_usuarios)
        
        endereco = validar_input(regex_endereco
                            ,'\nDigite o endereço ou "C" para cancelar\nFormato: "logradouro, nro - bairro - cidade/UF"): '
                            ,'Endereço inválido! Formato esperado: "Rua Exemplo, 123 - Centro - Cidade/SP"')
        data_nascimento = validar_input(regex_data_nascimento
                            ,'\nDigite a data de nascimento (dd/mm/aaaa) ou "C" para cancelar: '
                            ,'Data inválida! Use o formato dd/mm/aaaa')
        
        if nome.capitalize()=='C' or cpf.capitalize()=='C' or endereco.capitalize()=='C' or data_nascimento.capitalize=='C':
            return None
            
        usuario = {
            'nome' : nome
            ,'cpf' : cpf
            ,'data_nascimento' : data_nascimento
            ,'endereco' : endereco
        }

        lista_usuarios.append(usuario)
        print('\nUsuário criado com sucesso! \n')

        return lista_usuarios
          

def criar_conta(lista_usuarios, lista_contas):

    if lista_usuarios:

        pergunta = '\n---------------------------------------\nPara qual usuário a conta será criada?\n'

        for i, usuario in enumerate(lista_usuarios):
            pergunta = f'{pergunta}\n{i} - {usuario['nome']}'

        try:
            index_usuario = int(input(f'{pergunta}\n\n> '))
        except:
            print('!!! Digite uma das opções da lista !!!')
            criar_conta(lista_usuarios, lista_contas)

        if index_usuario > len(lista_usuarios) or index_usuario < 0:
            print('!!! Digite uma das opções da lista !!!')
            criar_conta(lista_usuarios, lista_contas)

        cpf_usuario = lista_usuarios[index_usuario]['cpf']
        
        numero = 1 if not lista_contas else len(lista_contas) + 1

        conta = {
            'agencia' : '0001'
            ,'numero' : numero
            ,'cpf_usuario' : cpf_usuario
            ,'saldo' : 0.00
            ,'saques' : 0
            ,'extrato' : ''
        }

        lista_contas.append(conta)
        print(f'\nConta {numero} criada com sucesso para o usuário {usuario['nome']}!\n')

        return lista_contas
    
    print('\n!!! Cadastre um usuário antes de criar um conta !!!\n')


def definir_conta_operacao(lista_usuarios, lista_contas, usuario = None):
    
    if lista_usuarios and lista_contas:
    
        if not usuario:
        
            pergunta = '\n---------------------------------------\nPara qual usuário deseja realizar operações?\n'

            for i, usuario in enumerate(lista_usuarios):
                pergunta = f'{pergunta}\n{i} - {usuario['nome']}'

            try:
                index_usuario = int(input(f'{pergunta}\n\n> '))
            except:
                print('\n!!! Digite uma das opções da lista !!!\n')
                definir_conta_operacao(lista_usuarios, lista_contas)

            if index_usuario > len(lista_contas) or index_usuario < 0:
                print('\n!!! Digite uma das opções da lista !!!\n')
                definir_conta_operacao(lista_usuarios, lista_contas)

        usuario = lista_usuarios[index_usuario]
        cpf_usuario = usuario['cpf']
        contas_usuario = [conta for conta in lista_contas if conta['cpf_usuario'] == cpf_usuario]

        pergunta = '\n---------------------------------------\nPara qual conta deste usuário deseja realizar operações?\n'

        for i, conta in enumerate(contas_usuario):
            pergunta = f'{pergunta}\n{i} - {conta['numero']}'

        try:
            index_conta = int(input(f'{pergunta}\n\n> '))
        except:
            print('\n!!! Digite uma das opções da lista !!!\n')
            definir_conta_operacao(lista_usuarios, lista_contas, usuario)

        if index_conta > len(contas_usuario) or index_conta < 0:
            print('\n!!! Digite uma das opções da lista !!!\n')
            definir_conta_operacao(lista_usuarios, lista_contas, usuario)

        conta = contas_usuario[index_conta]

        return conta

    print('\n!!! Não há usuários ou contas cadastradas !!!\n')


def definir_acao(lista_contas, lista_usuarios):
    
    while True:
        try:
            acao = int(input(TEXTO_ACOES))
        except:
            print('\n!!! Digite uma das opcoes do menu !!!\n')
            definir_acao(lista_contas, lista_usuarios)

        if acao not in ACOES:
            print('\n!!! Digite uma das opções do menu !!!\n')
            definir_acao(lista_contas, lista_usuarios)

        if acao == 1:
            lista_usuarios = criar_usuario(lista_usuarios)
        elif acao == 2:
            lista_contas = criar_conta(lista_usuarios, lista_contas)
        elif acao == 3:
            conta = definir_conta_operacao(lista_usuarios, lista_contas)
            lista_contas = definir_operacao(f'{TEXTO_QUAL_OPERACAO}', lista_contas, conta)
        else:
            return lista_usuarios, lista_contas

lista_usuarios, lista_contas = definir_acao(lista_contas, lista_usuarios)
