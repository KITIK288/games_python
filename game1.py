# Это игра угадай число на питон

import random

def game():
    comp_num = random.randint(1, 10)
    print("Компьютер загадал случайное число, в диапозоне от 1 до 10, попробуйте угадать его")
    player_num = int(input())
    counter = 0
    while 1:
        if player_num == comp_num:
            print("Вы победили, угадав число")
            counter += 1
            break
        elif player_num < comp_num:
            print("Ваше число меньше числа, загаданного компьютером, попробуйте снова")
            player_num = int(input())
            counter += 1
        elif player_num > comp_num:
            print("Ваше число больше числа, загаданного компьютером, попробуйте снова")
            player_num = int(input())
            counter += 1

    if counter == 1:
        print("Вы победили за ", counter, "ход")
    elif counter == 2 or counter == 3 or counter == 4:
        print("Вы победили за ", counter, "хода")
    else:
        print("Вы победили за ", counter, "ходов")

game()