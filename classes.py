from abc import ABC, abstractmethod
class Cliente():
    def __init__(self, nome : str, cpf : str, senha : str):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__clientes = []

class OperacoesFinanceiras(ABC):

    @abstractmethod
    def sacar(self,valor):
        pass

    @abstractmethod
    def deposito(self,valor):
        pass

    @abstractmethod
    def consultar_saldo(self):
        pass
        

class Banco():
    def __init__(self):
        pass

class Conta():
    def __init__(self,):
        pass

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

class Extrato():
    pass
