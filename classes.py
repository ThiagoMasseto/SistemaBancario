from abc import ABC, abstractmethod
class Cliente():
    def __init__(self, nome : str, cpf : str, senha : str):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__clientes = []
        

class Banco():
    def __init__(self):
        pass

class Conta():
    def __init__(self):
        pass

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

class Extrato():
    pass
