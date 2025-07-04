max_saques = 3
limite_saque = 500.00
saldo = 0.00
extrato = ''
saques = 0

operacoes = [1,2,3,4]
tipo_operacao = 0

QUAL_OPERACAO = '''
---------------------------------------
Qual operação deseja realizar?
'''

OUTRA_OPERACAO = '''
---------------------------------------
Realizar outra operacao?
'''

OPCOES_OPERACAO = '''
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

def Realizar_Deposito(mensagem = ''):
    global saldo, extrato

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
            Realizar_Deposito(mensagem)
    
def Realizar_Saque(mensagem = ''):
    global saldo, saques, extrato

    if saques != 3:
    
        if mensagem != '':
            print(mensagem)
        resposta = input(TEXTO_SAQUE)

        if resposta.upper() != 'C':
            try:
                valor_saque = float(resposta)
                if (valor_saque > 1500):
                    mensagem = f'\n---------------------------------------\nValor do saque maior que o limite permitido!\n'
                    Realizar_Saque(mensagem)
                elif valor_saque > saldo:
                    mensagem = f'\n---------------------------------------\nSaldo insuficiente!\n'
                    Realizar_Saque(mensagem)
                else:
                    saldo -= valor_saque
                    saques += 1
                    extrato = f'{extrato}\n-------------------------------\nSaque no valor de R$ {valor_saque:.2f}'
            except:
                mensagem = f'\n---------------------------------------\nDigite o valor desejado ou pressione \'C\' para cancelar!\n'
                Realizar_Deposito(mensagem)
    else:
        print(f'\n---------------------------------------\nO limite diário da quantidade de saques já foi atingido!\n')

def Visualizar_Extrato():

    print(f'\nEXTRATO:\n{extrato}\n\nSaldo: R$ {saldo:.2f}')
          

def Definir_Operacao(pergunta):
    global tipo_operacao
    
    try:
        tipo_operacao = int(input(f'{pergunta}{OPCOES_OPERACAO}'))
    except:
        print('\nDigite apenas uma das opções do menu!\n')
        Definir_Operacao(pergunta)
    
    if tipo_operacao not in operacoes:
        print('\nDigite apenas uma das opções do menu!\n')
        Definir_Operacao(pergunta)

    while tipo_operacao in operacoes:
        
        if tipo_operacao == 1:
            Realizar_Deposito()
            Definir_Operacao(OUTRA_OPERACAO)
        elif tipo_operacao == 2:
            Realizar_Saque()
            Definir_Operacao(OUTRA_OPERACAO)
        elif tipo_operacao == 3:
            Visualizar_Extrato()
            Definir_Operacao(OUTRA_OPERACAO)
        else:
            if tipo_operacao != 4:
                Definir_Operacao(OUTRA_OPERACAO)
            tipo_operacao = 0

Definir_Operacao(QUAL_OPERACAO)





    





