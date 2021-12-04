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
        desenha_forca(len(letras_erradas))
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
        print(f"Tentativas restantes: {7 - len(letras_erradas)}")

        if list(palavra_secreta) == letras_acertadas:
            acertou = True
            imprime_mensagem_vencedor()
        if len(letras_erradas) == 7:
            enforcou = True
            imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("       {}           {}")
    print("         \  _---_  /")
    print("          \/     \/")
    print("           |() ()|")
    print("            \ + /")
    print("           / HHH  \\")
    print("          /  \_/   \\")
    print("        {}          {}")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogo()
