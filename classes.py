from abc import ABC, abstractmethod
class Cliente():
    def __init__(self, nome : str, cpf : str, senha : str):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__clientes = []

    def getNome(self):
        return self.__nome
    def getCpf(self):
        return self.__cpf
    def getSenha(self):
        return self.__senha
    
    def setNome(self, nome):
        self.__nome = nome
    def setCpf(self,cpf):
        self.__cpf = cpf
    def setSenha(self, senha):
        self.__senha = senha
        

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
    def __init__(self,):
        pass

class Conta():
    def __init__(self,nome : str, cpf : str, senha : str, saldo : float):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__saldo = saldo
        self.__contas =[]
        
    def getNome(self):
        return self.__nome
    def getCpf(self):
        return self.__cpf
    def getSenha(self):
        return self.__senha
    def getSaldo(self):
        return self.__saldo
    
    def setNome(self, nome):
        self.__nome = nome
    def setNome(self, cpf):
        self.__cpf = cpf
    def setNome(self, senha):
        self.__senha = senha
    def setNome(self, saldo):
        self.__saldo = saldo
    

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

class Extrato():
    pass
