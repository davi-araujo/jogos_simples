import adivinhacao
import forca
import jogo_da_velha
import blackjack
import os
import time


def clear():
    os.system('cls')


def printa_menu():
    clear()
    print("***************************")
    print("Bem vindo ao menu de jogos!")
    print("***************************")
    print("(1) Jogo da forca", "(2) Jogo de adivinhação", "(3) Jogo da velha", "(4) BlackJack", sep="\n")


def escolhe_jogo():
    printa_menu()

    jogo = int(input("Escolha seu jogo: "))

    if jogo == 1:
        forca.jogo()
    elif jogo == 2:
        adivinhacao.jogo()
    elif jogo == 3:
        jogo_da_velha.jogo()
    elif jogo == 4:
        blackjack.jogo()
    else:
        clear()
        print("Escolha inválida. Por favor, escolha uma opção válida.")
        time.sleep(3)


if __name__ == "__main__":
    escolhe_jogo()
