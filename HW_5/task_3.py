""" Напишите игру "Крестики-нолики"."""

from random import randint
import os

def print_board(array:[list]):
    print('|', end=' ')
    print(*range(len(array)), sep=' | ',end=' | \n')
    print('-' * 13)
    for i, line in enumerate(array):        
        print('|', end=' ')
        print(*line, sep=' | ', end=f' | {i}\n')
        print('-' * 13)

def check(array):
    if array[0][0] == array[0][1] == array[0][2] != ' ' or array[1][0] == array[1][1] == array[1][2] != ' ' or array[2][0] == array[2][1] == array[2][2] != ' ':
        return True
    if array[0][0] == array[1][0] == array[2][0] != ' ' or array[0][1] == array[1][1] == array[2][1] != ' ' or array[0][2] == array[1][2] == array[2][2] != ' ':
        return True
    if array[0][0] == array[1][1] == array[2][2] != ' ' or array[2][0] == array[1][1] == array[0][2] != ' ':
        return True

if __name__ == '__main__':
    lst = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print('Начинаем игру крестики- нолики')
    players = ['0', 'X']
    turn = randint(0, 1)
    player = players[turn]
    print_board(lst)
    while True:
        print(f'Ходит {player}')
        row, col = [int(i) for i in input('укажите строку и столбец через пробел: ').split()]
        os.system('cls')
        lst[row][col] = player
        print_board(lst)
        if check(lst):
           print(f'Победили {player}')
           break
        else:
           turn = not turn
           player = players[turn]
