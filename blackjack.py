import random
from operator import itemgetter
import os

naipe = 0
valor = 0
estouro = False


def clear():
    os.system('cls')


# função que inicia o baralho com todas as cartas
def inicia_baralho():
    p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    o = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    baralho = [p, e, c, o]

    return baralho


# função que faz a soma das cartas do jogador
def soma(mao):
    clear()
    print("\n\n")
    global estouro
    banco = []

    soma_cartas = 0

    for i in mao:
        if i == 11:
            soma_cartas += 10
            print('J', end=' ')
        elif i == 12:
            soma_cartas += 10
            print('Q', end=' ')
        elif i == 13:
            soma_cartas += 10
            print('K', end=' ')
        elif i == 1:
            banco.append(i)
            print('A', end=' ')
        elif 1 < int(i) < 11:
            soma_cartas += i
            print(i, end=' ')

    for i in banco:
        if i == 1:
            if soma_cartas + 11 > 21:
                soma_cartas += 1
            else:
                soma_cartas += 11

    print("\n\nValor na mão: ", soma_cartas)

    if soma_cartas > 21:
        estouro = True

    return soma_cartas


# função do jogo em si
def jogo():
    clear()
    global naipe, valor, estouro
    baralho = inicia_baralho()
    cont = 0
    jogadores = []

    quant_jogadores = int(input("Informe a quantidade de jogadores: "))

    while cont != quant_jogadores:
        nome = input("Insira o nome do jogador que vai jogar: ")
        estouro = False
        escolha = 1
        carta = 0
        mao = []

        while carta == 0:
            naipe = random.randrange(0, 4)
            valor = random.randrange(0, 13)
            carta = baralho[naipe][valor]


        baralho[naipe][valor] = 0
        mao.append(carta)
        carta = 0

        while carta == 0:
            naipe = random.randrange(0, 4)
            valor = random.randrange(0, 13)
            carta = baralho[naipe][valor]

        baralho[naipe][valor] = 0
        mao.append(carta)

        soma_cartas = soma(mao)

        while escolha != 0:
            print("Quer outra carta?", "(1) Sim", "(0) Não")
            escolha = int(input("Digite: "))

            if escolha == 1:
                carta = 0
                while carta == 0:
                    naipe = random.randrange(0, 4)
                    valor = random.randrange(0, 13)
                    carta = baralho[naipe][valor]

                baralho[naipe][valor] = 0
                mao.append(carta)

                soma_cartas = soma(mao)

            if estouro:
                escolha = 0
                print("Passou de 21... Sinto muito")

        t = (nome, soma_cartas)
        jogadores.append(t)

        baralho = inicia_baralho()

        cont += 1

    clear()

    jogadores.sort(key=itemgetter(1), reverse=True)

    nao_estourou = []
    perdedores = []
    for i in jogadores:
        if i[1] < 22:
            nao_estourou.append(i)
        else:
            perdedores.append(i)

    print("\nEsses foram os que não estouraram: ")

    for i in nao_estourou:
        print(f'{i[0]} -> {i[1]} pontos')

    print("\nO vencedor (ou vencedores, em caso de empate) está no topo\nResto dos jogadores: ")

    for i in perdedores:
        print(f'{i[0]} -> {i[1]} pontos')


if __name__ == "__main__":
    jogo()
