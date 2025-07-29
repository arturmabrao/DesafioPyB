# Desafio de sistema bancário simples em Python

e = ''
operation = 'I'
count_wrong_command, limit_wrong_command = 0, 3
lst_operations = ('C', 'D', 'S', 'F', 'E')

balance, count_w, withdraw_value = 0, 0, 0
lst_withdraw_values = []
limit_w, deposite_value = 500, 1500 

while operation != 'F':
    operation = input('\n\nOperacoes:\n' 
    'C - Consultar saldo\n' \
    'D - Depositar\n' \
    'S - Sacar\n' \
    'F - Finalizar\n' \
    'E - Extrato\n' \
    ' Para sair Qual operacao deseja realizar? ').upper()
    
    if operation not in lst_operations:
        count_wrong_command+=1
        print('\nComando nao encontrado.')
        if count_wrong_command >= limit_wrong_command:
            print(f'APOS {limit_wrong_command} TENTATIVAS EQUIVOCADAS CONSECUTIVAS, '+
                  'A OPERACAO SERA ENCERRADA')
            break
        else:
            continue
    
    count_wrong_command=0

    if operation == 'F':
        break
    elif operation == 'C':
        print(f'\nValor do seu saldo: R${balance:.2f}')
    elif operation == 'S':
        if count_w > 2:
            print('\nVoce ja realizou 3 saques no dia de hoje')
            continue
        withdraw_value = float(input('Qual valor deseja sacar? R$'))
        if withdraw_value < 0:
            print('\nO valor de um saque deve ser positivo')
            continue
        elif withdraw_value > balance:
            print(f'\nVoce nao pode sacar R${withdraw_value:.2f}, '+
                  f'pois seu saldo e de R${balance:.2f}')
            continue
        elif withdraw_value > limit_w:
            print(f'\nVoce nao pode sacar {withdraw_value} '+
                  f'pois seu limite de valor por saque {limit_w}')
            continue
        else:
            try:
                balance-=withdraw_value
                lst_withdraw_values.append(withdraw_value)
                count_w+=1
                print(f'\nApos o saque, o valor do seu saldo e: {balance:.2f}')
            except e:
                print(e)
    elif operation == 'D':
        deposite_value = float(input('\nQual valor deseja depositar? R$'))
        if deposite_value < 0:
            print('\nO valor de um deposito ser positivo')
            continue
        else:
            try:
                balance+=deposite_value
                print(f'\nApos o deposito, o valor do seu saldo e: {balance:.2f}')
            except e:
                print (e)            
    elif operation == 'E':
        mesage_complement = ', os valores foram: '
        formatted_w_values = [f'{w:.2f}' for w in lst_withdraw_values]
        print(f'Extrado: \n- Seu saldo e de R${balance:.2f}'+ 
              f'\n- Voce relizou {count_w} saques no dia de hoje', end='') 
        print(mesage_complement if count_w else '.', end='')
        print(*formatted_w_values, sep=', ')        
    

print('\nOperacao Finalizada.\nAté a próxima.')