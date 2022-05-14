# IDEIA DE SISTEMA PARA MATRIZ UNIFICADA
# 0 => VAZIO
# 1 => BARCO
# 2 => VAZIO ATACADO
# 3 => BARCO ATACADO

import os
import random

comando = os.system
letras_linhas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
barcos = (3, 3, 2, 2)
pontos_impacto = sum(barcos)

# FUNCIONALIDADES


def gerador_matriz():
    linhas = []
    colunas = []
    for j in range(0, 10):
        colunas.append(0)
    for i in range(0, 10):
        linhas.append(colunas[:])
    return linhas[:]


def pega_letra_linha(num):
    return letras_linhas[num]


def pega_numero_linha(char):
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
            print('\033[31m O valor deve conter apenas dois digitos, '
                  'o primeiro referente à linha e o segundo à coluna \033[m')
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


def jogada(jogando, turno, player):
    player['num_tentativas'] += 1
    [linha, coluna] = entrada_jogador() if turno else ataque_computador()
    if player['casas'][linha][coluna]:
        player['tentativas'][linha][coluna] = True
        player['acertos'] += 1
        # TODO: Imedir que seja considerado um ponto acertado duas vezes
        if player['acertos'] == pontos_impacto:
            jogando = False
            # renderiza_tela(jogador, computador)
            print(f'\nParabens, voce VENCEU com {player["num_tentativas"]} tentativas!!!') if turno \
                else print(f'\nQue pena, voce PERDEU com {player["num_tentativas"]} tentativas do computador...')
    else:
        player['tentativas'][linha][coluna] = True
    turno = not turno
    return jogando, turno, player


def finalizar():
    sair = input('Deseja sair do jogo? (S/N) ')
    if sair.upper() == 'S':
        limpar_tela()
        comando('index.py')
    else:
        limpar_tela()
        comando('.\\batalha-naval\\index.py')


# DESENHO DE TELA


def cabecalho(mensagem):
    print('\n   ----------------------------')
    print(f'         {mensagem}       ')
    print('   ----------------------------\n')
    print('   ', end='')
    for contador in range(0, 10):
        print(f' {contador} ', end="")
        contador += 1
    print('')


def placar(acertos_jogador, acertos_computador):
    print('\n   ============================')
    print(f'   ||  PLAYER: {acertos_jogador}             ||')
    print(f'   ||  COMPUTADOR: {acertos_computador}         ||')
    print('   ============================')


def campo(mensagem, casas, tentativas, exibir_barcos=False):
    cabecalho(f'{mensagem}')
    for linha_matriz in range(0, len(casas)):
        print(f' {pega_letra_linha(linha_matriz)} ', end='')
        for coluna_matriz in range(0, len(casas[linha_matriz])):
            if tentativas[linha_matriz][coluna_matriz] and not casas[linha_matriz][coluna_matriz]:
                print('\033[1;31;44m X \033[m', end="")
            elif tentativas[linha_matriz][coluna_matriz] and casas[linha_matriz][coluna_matriz]:
                print('\033[7;31m x \033[m', end="")
            elif exibir_barcos and casas[linha_matriz][coluna_matriz]:
                print('\033[47m   \033[m', end="")
            else:
                print('\033[0;30;44m   \033[m', end="")
        print('')


def renderiza_tela(jogador, computador):
    limpar_tela()
    placar(jogador['acertos'], computador['acertos'])
    campo('CAMPO DO PLAYER', computador['casas'], computador['tentativas'], True)
    campo('CAMPO DO COMPUTADOR', jogador['casas'], jogador['tentativas'])


def limpar_tela():
    comando('cls' if os.name == 'nt' else 'clear')
