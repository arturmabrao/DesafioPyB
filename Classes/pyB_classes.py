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

class Deposito():
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque():
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

class Historico():

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
        self._cliente  = Cliente()
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