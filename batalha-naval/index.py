# TODO: Criar um sistema de inicialização de variáveis
from bn import gerador_matriz, posiciona_barcos, renderiza_tela, jogada, finalizar

jogador = {
    'casas': gerador_matriz(),
    'tentativas': gerador_matriz(),
    'acertos': 0,
    'num_tentativas': 0
}

computador = {
    'casas': gerador_matriz(),
    'tentativas': gerador_matriz(),
    'acertos': 0,
    'num_tentativas': 0
}

jogando = turno_jogador = True
posiciona_barcos(computador['casas'])
posiciona_barcos(jogador['casas'])
while jogando:
    renderiza_tela(jogador, computador)
    if turno_jogador:
        [jogando, turno_jogador, jogador] = jogada(jogando, turno_jogador, jogador)
    else:
        [jogando, turno_jogador, computador] = jogada(jogando, turno_jogador, computador)
finalizar()
