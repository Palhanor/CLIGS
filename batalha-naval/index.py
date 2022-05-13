# IDEIA DE SISTEMA PARA MATRIZ UNIFICADA
# 0 => VAZIO
# 1 => BARCO
# 2 => VAZIO ATACADO
# 3 => BARCO ATACADO

import random
import os

# TODO: Corrigir duplicação de código: campo_jogador e campo_computador; jogada_jogador e jogada_computador
# Variaveis gerais
reiniciar = True
jogando = True
turno_jogador = True
comando = os.system
barcos = [3, 3, 2, 2]
pontos_impacto = sum(barcos)
letras_linhas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')

# Variaveis jogador
acertos_jogador = 0
num_tentativas_jogador = 0
casas_jogador = [
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
tentativas_jogador = [
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

# Variaveis computador
acertos_computador = 0
num_tentativas_computador = 0
casas_computador = [
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
tentativas_computador = [
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


def pega_letra_linha(num):
    return letras_linhas[num]


def pega_numero_linha(char):
    return letras_linhas.index(char.upper())


def cabecalho(mensagem):
    print(f'\n{mensagem}\n')
    print('   ', end='')
    for contador in range(0, 10):
        print(f' {contador} ', end="")
        contador += 1
    print('')


def campo_jogador():
    cabecalho(' -=-=-=-= CAMPO DO PLAYER =-=-=-=- ')
    for linha_matriz in range(0, len(casas_computador)):
        print(f' {pega_letra_linha(linha_matriz)} ', end='')
        for coluna_matriz in range(0, len(casas_computador[linha_matriz])):
            if tentativas_computador[linha_matriz][coluna_matriz] and not casas_computador[linha_matriz][coluna_matriz]:
                print('\033[1;31;44m X \033[m', end="")
            elif tentativas_computador[linha_matriz][coluna_matriz] and casas_computador[linha_matriz][coluna_matriz]:
                print('\033[7;31m x \033[m', end="")
            elif casas_computador[linha_matriz][coluna_matriz]:
                print('\033[47m   \033[m', end="")
            else:
                print('\033[0;30;44m   \033[m', end="")
        print('')


def campo_computador():
    cabecalho(' -=-=-= CAMPO DO COMPUTADOR =-=-=- ')
    for linha_matriz in range(0, len(casas_jogador)):
        print(f' {pega_letra_linha(linha_matriz)} ', end='')
        for coluna_matriz in range(0, len(casas_jogador[linha_matriz])):
            if tentativas_jogador[linha_matriz][coluna_matriz] and not casas_jogador[linha_matriz][coluna_matriz]:
                print('\033[1;31;44m X \033[m', end="")
            elif tentativas_jogador[linha_matriz][coluna_matriz] and casas_jogador[linha_matriz][coluna_matriz]:
                print('\033[7;31m x \033[m', end="")
            else:
                print('\033[0;30;44m   \033[m', end="")
        print('')


def entrada_jogador():
    valido = False
    while not valido:
        valores = input('\nInsira o ponto da matriz: ')
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


def ataque_computador():
    # TODO: Impedir que o computador jogue duas vezes no mesmo ponto
    [linha, coluna] = posicoes(9)
    return linha, coluna


def posicoes(limite):
    # TODO: Impedir que os barcos fiquem uns sobre os outros
    posicao_linha = random.randint(0, limite)
    posicao_coluna = random.randint(0, limite)
    return posicao_linha, posicao_coluna


def tela():
    comando('cls')
    print(f'\nPLAYER: {acertos_jogador}')
    print(f'COMPUTADOR: {acertos_computador}')
    campo_jogador()
    campo_computador()


def posiciona_barcos(matriz):
    for barco in barcos:
        [posicao_linha, posicao_coluna] = posicoes(7)
        horizontal = True if random.randint(0, 1) == 1 else False
        for contador in range(0, barco):
            if horizontal:
                matriz[posicao_linha][posicao_coluna + contador] = True
            else:
                matriz[posicao_linha + contador][posicao_coluna] = True
        # print(f'foi sorteado a linha {posicao_linha} e a coluna {posicao_coluna}')


def jogada_jogador():
    global acertos_jogador, num_tentativas_jogador, jogando, turno_jogador
    [linha, coluna] = entrada_jogador()
    if casas_jogador[linha][coluna]:
        tentativas_jogador[linha][coluna] = True
        acertos_jogador += 1
        # TODO: Não contabilizar quando for acertado o mesmo lugar
        if acertos_jogador == pontos_impacto:
            jogando = False
            tela()
            print(f'\nParabens, voce VENCEU com {num_tentativas_jogador + 1} tentativas!!!')
    else:
        tentativas_jogador[linha][coluna] = True
    num_tentativas_jogador += 1
    turno_jogador = False


def jogada_computador():
    global acertos_computador, num_tentativas_computador, jogando, turno_jogador
    [linha, coluna] = ataque_computador()
    if casas_computador[linha][coluna]:
        tentativas_computador[linha][coluna] = True
        acertos_computador += 1
        if acertos_computador == pontos_impacto:
            jogando = False
            tela()
            print(f'\nQue pena, voce PERDEU com {num_tentativas_computador + 1} tentativas do computador...')
    else:
        tentativas_computador[linha][coluna] = True
    num_tentativas_computador += 1
    turno_jogador = True


while reiniciar:
    posiciona_barcos(casas_computador)
    posiciona_barcos(casas_jogador)
    while jogando:
        tela()
        if turno_jogador:
            jogada_jogador()
        else:
            jogada_computador()
    sair = input('Deseja sair do jogo? ')
    if sair.upper() == 'S':
        reiniciar = False
        comando('cls')
        comando('C:\\Users\\Computador\\Desktop\\CLIGS\\index.py')
    else:
        comando('cls')
        comando('C:\\Users\\Computador\\Desktop\\CLIGS\\batalha-naval\\index.py')
