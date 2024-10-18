# Игра камень ножницы бумага на python
# далее игра будет работать в окне tk

import random

def game():

    print("Это игра камень ножницы бумага")
    print("Выберите: 1 - камень, 2 - ножницы или 3 - бумага?")
    player_choice = int(input())
    comp_choice = random.randint(1, 3)

    if player_choice == 1:
        player_choice = "камень"
    elif player_choice == 2:
        player_choice = "ножницы"
    elif player_choice == 3:
        player_choice = "бумага"
    if comp_choice == 1:
        comp_choice = "камень"
    elif comp_choice == 2:
        comp_choice = "ножницы"
    elif comp_choice == 3:
        comp_choice = "бумага"

    print("Ваш выбор -", player_choice)
    print("Компьютер выбрал -", comp_choice)

    if player_choice == comp_choice:
        print("Ваш выбор -", player_choice, ". Выбор компьютера -", comp_choice, ". Итог - ничья")
    elif player_choice == "камень" and comp_choice == "ножницы":
        print("Камень бьёт ножницы. Вы победили.")
    elif player_choice == "камень" and comp_choice == "бумага":
        print("Бумага бьёт камень. Компьютер победил.")
    elif player_choice == "ножницы" and comp_choice == "камень":
        print("Камень бьёт ножницы. Компьютер победил.")
    elif player_choice == "ножницы" and comp_choice == "бумага":
        print("Ножницы режут бумагу. Вы победили")
    elif player_choice == "бумага" and comp_choice == "камень":
        print("Бумага бьёт камень. Вы победили")
    elif player_choice == "бумага" and comp_choice == "ножницы":
        print("Ножницы режут бумагу. Компьютер победил")

game()