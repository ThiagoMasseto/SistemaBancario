import os
import time
def menu():
    while True:
        escolha=int(input("Bem vindo ao Menu de opções!\nEscolha a opção que deseja\n1-Cadastrar Cliente\n2-" \
        "Criar Conta\n3-Acessar Conta\n4-Sair"))
        match escolha:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                print("Saindo... Até logo!")
                time.sleep("2")
                os.system("cls")
            case _:
                print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
                time.sleep("1.5")
                os.system("cls")
