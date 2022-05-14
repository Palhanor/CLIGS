import os

print('Lista de jogos: \n')
print('''
1 - Batalha naval
2 - Par ou impar
3 - Jokenpô
4 - Tic tac toe
5 - Pong
\n''')
selecionado = input('Qual você deseja jogar? ')

if selecionado == '1':
    os.system('cls')
    os.system('.\\batalha-naval\\index.py')
else:
    print('Lamentamos, mas este jogo está indisponível no momento...')

input('\nPressione ENTER para SAIR')
