import adivinhacao
import forca


def escolhe_jogo():
    print("***************************")
    print("Bem vindo ao menu de jogos!")
    print("***************************")

    print("(1) Jogo da forca", "(2) Jogo de adivinhação", sep="\n")

    jogo = int(input("Escolha seu jogo: "))

    if jogo == 1:
        forca.jogo()
    elif jogo == 2:
        adivinhacao.jogo()


if __name__ == "__main__":
    escolhe_jogo()
