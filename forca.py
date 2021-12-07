import random


def jogo():
    print("***************************")
    print("Bem vindo ao jogo da Forca!")
    print("***************************")

    palavras = []
    arquivo = open("palavras.txt", "r")

    for linha in arquivo:
        palavras.append(linha.strip())

    palavra_secreta = palavras[random.randrange(len(palavras))]
    letras_acertadas = ["_" for _letra in palavra_secreta]
    letras_erradas = []

    acertou = False
    enforcou = False

    for letra in letras_acertadas:
        print(letra, end=" ")
    print("")

    while not acertou and not enforcou:
        acertou_letra = False
        chute = input("Qual a letra?")
        chute = chute.strip()

        posicao = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[posicao] = letra
                acertou_letra = True
            print(letras_acertadas[posicao], end=" ")
            posicao += 1
        print("")

        if not acertou_letra:
            if chute in letras_erradas:
                print(f'A letra \'{chute.strip()}\' ja foi chutada')
            else:
                letras_erradas.append(chute)

        print("Letras que já foram: ", end="")

        for letras in letras_erradas:
            print(letras, end=" ")
        print("")
        print(f"Tentativas restantes: {6 - len(letras_erradas)}")

        if list(palavra_secreta) == letras_acertadas:
            acertou = True
            print("Voce escapou da forca")
        if len(letras_erradas) == 6:
            enforcou = True
            print("Voce morreu enforcado")

    print("Fim do jogo")


if __name__ == "__main__":
    jogo()
