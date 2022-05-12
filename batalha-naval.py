# CLIGS -> Command Line Interface Games

import random
import os

# TODO: Permitir que usuário jogue contra a máquina
# TODO: Permitir que usuário faça configurações nos valores
# sair = False
jogando = True
barcos = [3, 3, 2, 2]
pontos_impacto = sum(barcos)
acertos = num_tentativas = 0
letras_linhas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
casas = [
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False]
]
tentativas = [
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False]
]
comando = os.system


def pega_letra_linha(num):
    return letras_linhas[num]


def pega_numero_linha(char):
    return letras_linhas.index(char.upper())


def cabecalho():
    print('\n          BATALHA NAVAL\n')
    print('   ', end='')
    for contador in range(0, 10):
        print(f' {contador} ', end="")
        contador += 1
    print(' ')


def entrada():
    valido = False
    while not valido:
        valores = input('\nInsira o ponto da matriz (Ex: A2,C4, E7): ')
        if len(valores) != 2:
            print('O valor deve conter apenas dois digitos, o primeiro referente à linha e o segundo à coluna')
            continue
        elif valores[0].isdigit():
            print('O primeiro valor deve ser uma letra referente à linha a ser selecionada')
            continue
        elif not valores[0].isdigit() and valores[0].upper() not in letras_linhas:
            print('A linha indicada não é válida dentro do jogo')
            continue
        elif not valores[1].isdigit():
            print('O segundo valor deve ser um número referente à coluna a ser selecionada')
            continue
        else:
            [valor_linha, valor_coluna] = valores
            valor_linha = pega_numero_linha(valor_linha)
            valor_coluna = int(valor_coluna)
            return valor_linha, valor_coluna


def posicoes():
    # TODO: Impedir que os barcos fiquem uns sobre os outros
    posicao_linha = random.randint(0, 7)
    posicao_coluna = random.randint(0, 7)
    return posicao_linha, posicao_coluna


def tela():
    cabecalho()
    for linha_matriz in range(0, len(casas)):
        print(f' {pega_letra_linha(linha_matriz)} ', end='')
        for coluna_matriz in range(0, len(casas[linha_matriz])):
            if tentativas[linha_matriz][coluna_matriz] and not casas[linha_matriz][coluna_matriz]:
                print('\033[1;31;44m X \033[m', end="")
            elif tentativas[linha_matriz][coluna_matriz] and casas[linha_matriz][coluna_matriz]:
                print('\033[7;31m x \033[m', end="")
            else:
                print('\033[0;30;44m   \033[m', end="")
        print(' ')


def configuracoes():
    for barco in barcos:
        [posicao_linha, posicao_coluna] = posicoes()
        horizontal = True if random.randint(0, 1) == 1 else False
        for contador in range(0, barco):
            if horizontal:
                casas[posicao_linha][posicao_coluna + contador] = True
            else:
                casas[posicao_linha + contador][posicao_coluna] = True
        # print(f'foi sorteado a linha {posicao_linha} e a coluna {posicao_coluna}')


# TODO: Permitir que o usuário possa recomeçar o jogo
configuracoes()
while jogando:
    tela() if num_tentativas >= 1 else print('\n          BATALHA NAVAL\n')
    [linha, coluna] = entrada()
    if casas[linha][coluna]:
        tentativas[linha][coluna] = True
        comando('cls')
        acertos += 1
        # TODO: Não contabilizar quando for acertado o mesmo lugar
        if acertos == pontos_impacto:
            jogando = False
            comando('cls')
            tela()
            print(f'\nParabens, voce VENCEU com {num_tentativas + 1} tentativas!!!')
    else:
        tentativas[linha][coluna] = True
        comando('cls')
    num_tentativas += 1

input('\nPressione ENTER para SAIR')
