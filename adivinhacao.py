import random


def jogo():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(0, 101)
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha seu nível: "))

    if nivel == 1:
        total_de_tentativas = 10
    elif nivel == 2:
        total_de_tentativas = 7
    else:
        total_de_tentativas = 4

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = input("Digite um número entre 1 e 100: ")
        numero = int(chute)
        print("Você digitou", chute)

        if numero < 1 or numero > 100:
            print("Você deve digitar um número entre 1 e 100.")
            continue

        acertou = numero == numero_secreto
        maior = numero > numero_secreto
        menor = numero < numero_secreto

        if acertou:
            print(f"Você acertou o número! Sua pontuação foi de {pontos} pontos")
            break
        else:
            if maior:
                print("Você errou o número. O número secreto é menor que seu chute!")
            elif menor:
                print("Você errou o número. O número secreto é maior que seu chute!")

            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos

    print(f"Fim do jogo. O número secreto era", numero_secreto, end=".\n")


if __name__ == "__main__":
    jogo()
