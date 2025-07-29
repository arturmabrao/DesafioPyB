# Desafio de sistema bancário simples em Python

e = ''
operation = 'I'
balance, limit_w, withdraw_value, deposite_value, = 0, 0, 0, 1500

while operation > 'F' :
    operation = input("Operacoes:\n" 
    "C - Consultar saldo\n" \
    "D - Depositar\n" \
    "S - Sacar\n" \
    "F - Finalizar\n" \
    " Para sair Qual operacao deseja realizar? ").upper()

    if operation == 'F':
        break
    elif operation == 'C':
        print(f'Valor do seu saldo: {balance}')
    elif operation == 'S':
        withdraw_value = input("Qual valor deseja sacar?")
        if withdraw_value < 0:
            print("O valor de um saque deve ser positivo")
            continue
        elif withdraw_value > balance:
            print(f'Voce nao pode sacar {withdraw_value}, pois seu saldo e de {balance}')
            continue
        elif withdraw_value > limit_w:
            print(f'Voce nao pode sacar {withdraw_value} pois e maior que seu limite de saque disponivel {limit_w}')
        else:
            try:
                balance-=withdraw_value
                limit-=withdraw_value
                print(f'Apos o saque, o valor do seu saldo e: {balance}')
            except e:
                print(e)
    elif operation == 'D':
        deposite_value = input("Qual valor deseja depositar?")
        if deposite_value < 0:
            print("O valor de um deposito ser positivo")
            continue
        else:
            try:
                balance+=deposite_value
                print(f'Apos o deposito, o valor do seu saldo e: {balance}')
            except e:
                print (e)            


#    operation = 'F'

print("Finalizado.\nAté a próxima.")