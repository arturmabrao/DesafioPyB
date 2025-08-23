from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    @property
    @abstractmethod    
    def valor(conta):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas  = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Historico:

    def __init__(self):
        self._transacoes = []

    @property
    def transacaoes(self):
        return self._transacoes

    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%Y-%m-%d %H:%m:%s"),
            }
        )

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._agencia = '001'
        self._numero = numero
        self._cliente  = cliente #Cliente()
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo 
        
        if excedeu_saldo:
            print('\nSaldo excedido. Saque nao pode ser efetuado')
        elif valor > 0:
            self._saldo-=valor
            print('\nSaque efetuado')
            return True
        else:
            print('\nValor invalido. Saque nao pode ser efetuado')

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo+=valor
            print('\nDeposito efetuado')
            return True      
        else:
            print('\nValor invalido. Saque nao pode ser efetuado')

        return False
  
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=1500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.trasacoes 
             if transacao['tipo']==Saque.__name__]
        )

        saldo = self.saldo
        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques
        
        if excedeu_saques:
            print('\nLimite de saques excedido. Saque nao pode ser efetuado')
        if excedeu_limite > self.limite_saques:
            print('\nValor limite diario excedido. Saque nao pode ser efetuado')
        elif excedeu_saldo:
            print('\nSaldo excedido. Saque nao pode ser efetuado')
        else:
            if super.sacar(valor):
                self.limite+=valor
                return True
                 
        return False

    def __str__(self):
        return f'''\
            'Agencia: \t{self.agencia}
            'Numero: \t{self.numero}
            'Cliente: \t{self.cliente.nome}'''

def cria_conta(cliente,numero):
    conta = Conta(numero, cliente)
    cliente.adicionar_conta(conta)
    print(f'Conta {numero} criada')
    return conta

def cria_cliente():
    nome = input('Nome: ')
    cpf = input('CPF: ')
    endereco = input('Endereco: ')
    data_nascimento = input('Data de Nascimento: ')

    cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)
    return cliente

def seleciona_cliente(clientes):
    count = 1
    for c in clientes: 
        print(f'Id: {count}\tCliente: {c.nome}') 
        count+=1
    return int(input('Digite o Id do cliente: ').strip())-1

def seleciona_conta(contas):
    count = 1
    for c in contas: 
        print(f'Id: {count}\t Conta: {c.numero}') 
        count+=1
    return int(input('Digite o id da conta buscada: ').strip())-1


def  main():
    clientes, contas = [], []
    sequencial_conta = 1
    operacao = 'I'
    lst_operacoes = ('C', 'D', 'S', 'F', 'E', 'A', 'K')
    count_wrong_command, limit_wrong_command = 0, 3
    
    while operacao != 'F':
        operacao = input('\n\nOperacoes:\n' 
        'A - Adicionar Cliente\n' \
        'K - Criar Conta\n' \
        'C - Consultar saldo\n' \
        'D - Depositar\n' \
        'S - Sacar\n' \
        'E - Extrato\n' \
        'F - Finalizar\n' \
        ' Qual operacao deseja realizar? ').upper().strip()

        if operacao not in lst_operacoes:
            count_wrong_command+=1
            if count_wrong_command >= limit_wrong_command: 
                break 
            else: 
                continue

        count_wrong_command=0

        if operacao == 'F':
            break
        elif operacao == 'A':
            cliente = cria_cliente()
            clientes.append(cliente)
        elif operacao == 'K':
            if len(clientes) > 0:
                index_cliente = seleciona_cliente(clientes)
                conta = cria_conta(clientes[index_cliente], sequencial_conta)
                sequencial_conta=+1
                contas.append(conta)
            else:
                print('Primeiro cadastre um cliente.')
        elif operacao == 'C':
            if len(clientes) > 0:
                index_cliente = seleciona_cliente(clientes)
                cliente_sald = clientes[index_cliente]
                if len(cliente_sald.contas) > 0:
                    index_conta = seleciona_conta(cliente_sald.contas)
                    conta_sald = cliente_sald.contas[index_conta]
                    print(f'Cliente:\t{cliente.nome}\n'+
                          f'Conta:\t{conta_sald.numero}\n'+ 
                          f'Saldo:\t{conta.saldo}')
        
        elif operacao == 'D':
            if len(clientes) > 0:
                index_cliente = seleciona_cliente(clientes)
                cliente_depo = clientes[index_cliente]
                if len(cliente_depo.contas) > 0:
                    index_conta = seleciona_conta(cliente_depo.contas)
                    conta_depo = cliente_depo.contas[index_conta]
                    valor_depo = float(input(('Valor a depositar: ').strip()))
                    conta_depo.depositar(valor_depo)
                else:
                    print('Primeiro cadastre uma conta para este cliente.')                
            else:
                print('Primeiro cadastre um cliente.')
#        elif operacao == 'S':
#            show_balance()                
#        elif operacao == 'E':
#            get_bankstatement(balance, count_wvithdraw=count_wvithdraw)
#
    for c in contas:
        print(f'Conta {c.numero} cliente {c.cliente.nome}')
    print('\nOperacao Finalizada. Ate a proxima.')

main()