import os

print('\n   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
print('             LISTA DE JOGOS')
print('\n   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
print('''
   + - - - + - - - - - - - - - - - - +
   |  Num  |          Jogo           |
   + - - - + - - - - - - - - - - - - +
   |   1   |      Batalha naval      |
   + - - - + - - - - - - - - - - - - +
   |   2   |       Tic Tac Toe       |
   + - - - + - - - - - - - - - - - - +
   |   3   |         Jokenpô         |
   + - - - + - - - - - - - - - - - - +
   |   4   |       Par ou impar      |
   + - - - + - - - - - - - - - - - - +
''')

while True:
    selecionado = input('\n   Insira o número do jogo que você deseja começar: ')
    if selecionado == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('.\\batalha-naval\\index.py')
    else:
        print('   Lamentamos, mas este jogo está indisponível no momento. Por favor, escolha outro!')
