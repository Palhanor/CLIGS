# IDEIA DE SISTEMA PARA MATRIZ UNIFICADA
# 0 => VAZIO
# 1 => BARCO
# 2 => VAZIO ATACADO
# 3 => BARCO ATACADO

# TODO: Continuar a modularização

import random
import os

comando = os.system
letras_linhas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
barcos = (3, 3, 2, 2)
pontos_impacto = sum(barcos)


def gerador_matriz():
    """
    Formata uma amtriz 10 por 10 para ser usada como tabuleiro
    :return: Matriz 10 por 10 com valroes 0
    """
    linhas = []
    colunas = []
    for j in range(0, 10):
        colunas.append(0)
    for i in range(0, 10):
        linhas.append(colunas[:])
    return linhas[:]


def pega_letra_linha(num):
    """
    :param num: Número da linha da matriz
    :return: Letra respectiva da linha da matriz indicada
    """
    return letras_linhas[num]


def pega_numero_linha(char):
    """
    :param char: Letra da linha da matriz
    :return: Número respectivo das linha da matriz indicada
    """
    return letras_linhas.index(char.upper())


def gera_posicao(limite):
    # TODO: Impedir que os barcos fiquem uns sobre os outros
    posicao_linha = random.randint(0, limite)
    posicao_coluna = random.randint(0, limite)
    return posicao_linha, posicao_coluna


def posiciona_barcos(matriz):
    for barco in barcos:
        [posicao_linha, posicao_coluna] = gera_posicao(7)
        horizontal = True if random.randint(0, 1) == 1 else False
        for contador in range(0, barco):
            if horizontal:
                matriz[posicao_linha][posicao_coluna + contador] = True
            else:
                matriz[posicao_linha + contador][posicao_coluna] = True
        # print(f'foi sorteado a linha {posicao_linha} e a coluna {posicao_coluna}')


def ataque_computador():
    # TODO: Impedir que o computador jogue duas vezes no mesmo ponto
    [linha, coluna] = gera_posicao(9)
    return linha, coluna


def entrada_jogador():
    while True:
        valores = input('\nInsira o ponto da matriz: ')
        if len(valores) != 2:
            print('\033[31m O valor deve conter apenas dois digitos, o primeiro referente à linha e o segundo à coluna \033[m')
            continue
        elif valores[0].isdigit():
            print('\033[31m O primeiro valor deve ser uma letra referente à linha a ser selecionada \033[m')
            continue
        elif not valores[0].isdigit() and valores[0].upper() not in letras_linhas:
            print('\033[31m A linha indicada não é válida dentro do jogo \033[m')
            continue
        elif not valores[1].isdigit():
            print('\033[31m O segundo valor deve ser um número referente à coluna a ser selecionada \033[m')
            continue
        else:
            [valor_linha, valor_coluna] = valores
            valor_linha = pega_numero_linha(valor_linha)
            valor_coluna = int(valor_coluna)
            return valor_linha, valor_coluna


def cabecalho(mensagem):
    print('\n   ----------------------------')
    print(f'         {mensagem}       ')
    print('   ----------------------------\n')
    print('   ', end='')
    for contador in range(0, 10):
        print(f' {contador} ', end="")
        contador += 1
    print('')


def limpar_tela():
    comando('cls' if os.name == 'nt' else 'clear')


def finalizar():
    sair = input('Deseja sair do jogo? ')
    if sair.upper() == 'S':
        limpar_tela()
        comando('index.py')
    else:
        limpar_tela()
        comando('.\\batalha-naval\\index.py')
