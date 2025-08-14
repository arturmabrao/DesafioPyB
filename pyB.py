# Desafio de sistema bancário simples em Python

def input_value(oprt):
    input_val, value = 0, 0
    input_val = float(input(f'\nQual valor deseja {oprt}? R$').strip())

    if input_val <= 0: print(f'\nVoce nao pode {oprt} zero ou valor negativo')
    else: value = input_val
        
    return value

def quit():
    global break_loop
    break_loop = True

def wrong_command_action():
    global count_wrong_command, limit_wrong_command
    count_wrong_command+=1
    print('\nComando nao encontrado.')
    if count_wrong_command >= limit_wrong_command:
        quit()
        print(f'APOS {limit_wrong_command} TENTATIVAS EQUIVOCADAS CONSECUTIVAS, '+
                  'A OPERACAO ESTA SENDO ENCERRADA')
    return count_wrong_command

def show_balance():
    print(f'\nValor do seu saldo: R${balance:.2f}')
    return None

def get_bankstatement():
    global balance, count_wvithdraw, lst_withdraw_values
    mesage_complement = ', os valores foram:'
    formatted_w_values = [f'{w:.2f}' for w in lst_withdraw_values]
    print(f'\nExtrado: \n- Seu saldo e de R${balance:.2f}'+ 
          f'\n- Voce relizou {count_wvithdraw} saques no dia de hoje', end='') 
    print(mesage_complement if count_wvithdraw else '.', end='')
    print(' R$' if count_wvithdraw else '', end='')
    print(*formatted_w_values, sep=', R$', end='.')   

def action_withdraw(balance):
        local_balance, withdraw_value = balance, 0
        global count_wvithdraw, LIMIT_WITHDRAW, lst_withdraw_values
        if count_wvithdraw > 2:
            print('\nVoce ja realizou 3 saques no dia de hoje')
            return balance
        withdraw_value = input_value('sacar')
        if withdraw_value > local_balance:
            print(f'\nVoce nao pode sacar R${withdraw_value:.2f}, '+
                  f'pois seu saldo e de R${local_balance:.2f}')
            return local_balance
        elif withdraw_value > LIMIT_WITHDRAW:
            print(f'\nVoce nao pode sacar {withdraw_value} '+
                  f'pois seu limite de valor por saque {LIMIT_WITHDRAW}')
            return local_balance
        else:
            try:
                local_balance-=withdraw_value
                lst_withdraw_values.append(withdraw_value)
                count_wvithdraw+=1
                print(f'\nApos o saque, o valor do seu saldo e: {local_balance:.2f}')
                return local_balance
            except e:
                print(e)

def action_deposit(balance):
    local_balance, deposit_value = balance, 0
    deposit_value = input_value('depositar')

    if deposit_value > 0:
        try:
            local_balance+=deposit_value
            print(f'\nApos o deposito, o valor do seu saldo e: {local_balance:.2f}')
        except e:
            print (e)            
    return local_balance

e = ''
operation = 'I'
count_wrong_command, limit_wrong_command = 0, 3
break_loop = False
lst_operations = ('C', 'D', 'S', 'F', 'E')

balance, count_wvithdraw = 0, 0
lst_withdraw_values = []
LIMIT_WITHDRAW = 500

while operation != 'F':
    operation = input('\n\nOperacoes:\n' 
    'C - Consultar saldo\n' \
    'D - Depositar\n' \
    'S - Sacar\n' \
    'E - Extrato\n' \
    'F - Finalizar\n' \
    ' Qual operacao deseja realizar? ').upper().strip()
    
    if operation not in lst_operations:
        count_wrong_command = wrong_command_action()

        if break_loop: break
        else: continue
    
    count_wrong_command=0

    if operation == 'F':
        quit()
        if break_loop: break
        else: continue

    elif operation == 'C':
        show_balance()
    elif operation == 'S':
        balance = action_withdraw(balance)
    elif operation == 'D':
        balance = action_deposit(balance)
    elif operation == 'E':
        get_bankstatement()

print('\nOperacao Finalizada. Ate a proxima.')