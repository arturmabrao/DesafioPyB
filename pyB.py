# Desafio de sistema bancário simples em Python

e = ''
operation = 'I'
balance, count_w, limit_w, withdraw_value, deposite_value, = 0, 0, 500, 0, 1500

while operation != 'F':
    operation = input("\n\nOperacoes:\n" 
    "C - Consultar saldo\n" \
    "D - Depositar\n" \
    "S - Sacar\n" \
    "F - Finalizar\n" \
    " Para sair Qual operacao deseja realizar? ").upper()

    if operation == 'F':
        break
    elif operation == 'C':
        print(f'\nValor do seu saldo: {balance}')
    elif operation == 'S':
        if count_w > 2:
            print("\nVoce ja realizou 3 saques no dia de hoje")
            continue
        withdraw_value = float(input("Qual valor deseja sacar? "))
        if withdraw_value < 0:
            print("\nO valor de um saque deve ser positivo")
            continue
        elif withdraw_value > balance:
            print(f'\nVoce nao pode sacar {withdraw_value}, pois seu saldo e de {balance}')
            continue
        elif withdraw_value > limit_w:
            print(f'\nVoce nao pode sacar {withdraw_value} pois seu limite de valor por saque {limit_w}')
        else:
            try:
                balance-=withdraw_value
                count_w+=1
                print(f'\nApos o saque, o valor do seu saldo e: {balance}')
            except e:
                print(e)
    elif operation == 'D':
        deposite_value = float(input("\nQual valor deseja depositar? "))
        if deposite_value < 0:
            print("\nO valor de um deposito ser positivo")
            continue
        else:
            try:
                balance+=deposite_value
                print(f'\nApos o deposito, o valor do seu saldo e: {balance}')
            except e:
                print (e)            

print("\nOperacao Finalizada.\nAté a próxima.")