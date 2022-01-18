import os

velha = False
ganhou = False
linha = None
coluna = None
ganhador = None


def clear():
    os.system('cls')


# função que insere o símbolo
def insere_simbolo(lin, col, simbolo, linhas):
    if col == 'a':
        col = 1
    elif col == 'b':
        col = 2
    elif col == 'c':
        col = 3

    li = linhas[lin]

    if li[col] != ' ':
        print("Posição já preenchida. Perdeu a vez.")
        return linhas

    li[col] = simbolo

    linhas[lin] = li
    return linhas


# função que printa o jogo da velha
def printa_jogo(linhas):
    clear()
    texto = f'''
    {linhas[0][0]} {linhas[0][1]} {linhas[0][2]} {linhas[0][3]}
    {linhas[1][0]} {linhas[1][1]} {linhas[1][2]} {linhas[1][3]}
    {linhas[2][0]} {linhas[2][1]} {linhas[2][2]} {linhas[2][3]}
    {linhas[3][0]} {linhas[3][1]} {linhas[3][2]} {linhas[3][3]}
    '''
    print(texto)


# função que verifica se deu velha
def jogo_acabou(linhas):
    global velha
    global ganhou

    l1 = linhas[1]
    l2 = linhas[2]
    l3 = linhas[3]

    for li in linhas:
        if li[1] == li[2] and li[2] == li[3] and li[3] != ' ':
            simbolo = li[1]
            ganhou = True
            return simbolo

    for i in [1, 2, 3]:
        if l1[i] == l2[i] and l2[i] == l3[i] and l2[i] != ' ':
            simbolo = l1[i]
            ganhou = True
            return simbolo

    if l1[1] == l2[2] and l2[2] == l3[3] and l2[2] != ' ':
        simbolo = l1[i]
        ganhou = True
        return simbolo

    if l1[3] == l2[2] and l2[2] == l3[1] and l2[2] != ' ':
        simbolo = l1[i]
        ganhou = True
        return simbolo

    if ' ' in l1 or ' ' in l2 or ' ' in l3:
        velha = False
        return None
    else:
        velha = True
        return None


# função principal que gerencia o jogo
def jogo():
    # variáveis booleanas que organizam qual símbolo será marcado
    global linha, coluna, ganhador
    x = True
    o = False
    # variável booleana que auxilia a pegar a posição que será marcada
    primeira = True

    # linhas do jogo em si
    linha_da_info = [' ', 'a', 'b', 'c']
    linha_de_cima = [1, ' ', ' ', ' ']
    linha_do_meio = [2, ' ', ' ', ' ']
    linha_de_baixo = [3, ' ', ' ', ' ']
    linhas = [linha_da_info, linha_de_cima, linha_do_meio, linha_de_baixo]
    printa_jogo(linhas)

    while not velha and not ganhou:
        entrada = input('Insira a casa que deseja marcar (linha e coluna): ')

        # pegando a entrada que o usuario quer inserir o simbolo
        for i in entrada:
            if primeira:
                primeira = False
                linha = int(i)
            else:
                primeira = True
                coluna = i

        # inserindo os simbolos
        if x:
            linhas = insere_simbolo(linha, coluna, 'x', linhas)
            x = False
            o = True
        elif o:
            linhas = insere_simbolo(linha, coluna, 'o', linhas)
            x = True
            o = False

        ganhador = jogo_acabou(linhas)
        printa_jogo(linhas)

    if velha:
        print("O jogo acabou deu velha.")
    elif ganhou:
        print(f"O jogo acabou e o jogador do símbolo {ganhador} ganhou")


if __name__ == "__main__":
    jogo()
