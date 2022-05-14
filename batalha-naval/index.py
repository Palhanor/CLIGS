import bn

# TODO: Corrigir duplicação de código: campo_jogador e campo_computador; jogada_jogador e jogada_computador
# TODO: Criar um sistema de inicialização de variáveis

# JOGADORES
acertos_jogador = acertos_computador = 0
num_tentativas_jogador = num_tentativas_computador = 0
[casas_jogador, casas_computador] = [bn.gerador_matriz(), bn.gerador_matriz()]
[tentativas_jogador, tentativas_computador] = [bn.gerador_matriz(), bn.gerador_matriz()]


def campo_jogador():
    bn.cabecalho('CAMPO DO PLAYER ')
    for linha_matriz in range(0, len(casas_computador)):
        print(f' {bn.pega_letra_linha(linha_matriz)} ', end='')
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
    bn.cabecalho('CAMPO DO COMPUTADOR')
    for linha_matriz in range(0, len(casas_jogador)):
        print(f' {bn.pega_letra_linha(linha_matriz)} ', end='')
        for coluna_matriz in range(0, len(casas_jogador[linha_matriz])):
            if tentativas_jogador[linha_matriz][coluna_matriz] and not casas_jogador[linha_matriz][coluna_matriz]:
                print('\033[1;31;44m X \033[m', end="")
            elif tentativas_jogador[linha_matriz][coluna_matriz] and casas_jogador[linha_matriz][coluna_matriz]:
                print('\033[7;31m x \033[m', end="")
            else:
                print('\033[0;30;44m   \033[m', end="")
        print('')


def jogada_jogador():
    global acertos_jogador, num_tentativas_jogador, jogando, turno_jogador
    [linha, coluna] = bn.entrada_jogador()
    if casas_jogador[linha][coluna]:
        tentativas_jogador[linha][coluna] = True
        acertos_jogador += 1
        # TODO: Não contabilizar quando for acertado o mesmo lugar
        if acertos_jogador == bn.pontos_impacto:
            jogando = False
            renderiza_tela()
            print(f'\nParabens, voce VENCEU com {num_tentativas_jogador + 1} tentativas!!!')
    else:
        tentativas_jogador[linha][coluna] = True
    num_tentativas_jogador += 1
    turno_jogador = False


def jogada_computador():
    global acertos_computador, num_tentativas_computador, jogando, turno_jogador
    [linha, coluna] = bn.ataque_computador()
    if casas_computador[linha][coluna]:
        tentativas_computador[linha][coluna] = True
        acertos_computador += 1
        if acertos_computador == bn.pontos_impacto:
            jogando = False
            renderiza_tela()
            print(f'\nQue pena, voce PERDEU com {num_tentativas_computador + 1} tentativas do computador...')
    else:
        tentativas_computador[linha][coluna] = True
    num_tentativas_computador += 1
    turno_jogador = True


def renderiza_tela():
    bn.limpar_tela()
    print(f'\nPLAYER: {acertos_jogador}')
    print(f'COMPUTADOR: {acertos_computador}')
    campo_jogador()
    campo_computador()


jogando = turno_jogador = True
bn.posiciona_barcos(casas_computador)
bn.posiciona_barcos(casas_jogador)
while jogando:
    renderiza_tela()
    if turno_jogador:
        jogada_jogador()
    else:
        jogada_computador()
bn.finalizar()
