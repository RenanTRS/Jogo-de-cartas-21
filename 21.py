from random import randint
from time import sleep

opc = ''
cont = 1
carta = 0
soma = 0
rodada = []

print('=' * 30)
print('{:^30}'.format('Jogo de 21'))
print('=' * 30)

while True:
    print(f'{cont}º carta....')

    carta = randint(1, 13)
    soma += carta
    cont += 1

    if carta == 1:
        rodada.append('A')
    elif carta == 11:
        rodada.append('J')
    elif carta == 12:
        rodada.append('Q')
    elif carta == 13:
        rodada.append('K')
    else:
        rodada.append(carta)
    
    sleep(1.5)
    print(carta)
    print(f'\nSuas cartas: \033[1;33m{rodada}\033[m')
    print(f'Total: {soma}')
    print('=' * 30)

    if soma > 21:
        print('\033[1;31mVocê perdeu.\033[m')
        break
    elif soma == 21:
        print('\033[1;32mVocê ganhou.\033[m')
        break
    else:
        opc = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if opc == 'N':
            print('Saindo do jogo 21....')

            break

