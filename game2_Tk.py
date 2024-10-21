import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

comp_choice = random.randint(1, 3)

if comp_choice == 1:
    comp_choice = "камень"
elif comp_choice == 2:
    comp_choice = "ножницы"
elif  comp_choice == 3:
    comp_choice = "бумага"

def game_button1():
    player_choice = "камень"
    if player_choice == comp_choice:
        messagebox.showinfo("Информация",f"Вы выбрали одно и тоже. Итог - ничья")
    elif player_choice == "камень" and comp_choice == "ножницы":
        messagebox.showinfo("Информация", f"Камень бьёт ножницы. Вы победили.")
    elif player_choice == "камень" and comp_choice == "бумага":
        messagebox.showinfo("Информация", f"Бумага бьёт камень. Компьютер победил")

def game_button2():
    player_choice = "ножницы"
    if player_choice == comp_choice:
        messagebox.showinfo("Информация",f"Вы выбрали одно и тоже. Итог - ничья")
    elif player_choice == "ножницы" and comp_choice == "камень":
        messagebox.showinfo("Информация", f"Бумага бьёт камень. Компьютер победил")
    elif player_choice == "ножницы" and comp_choice == "бумага":
        messagebox.showinfo("Информация", f"Ножницы режут бумагу. Вы победили")

def game_button3():
    player_choice = "бумага"
    if player_choice == comp_choice:
        messagebox.showinfo("Информация", f"Вы выбрали одно и тоже. Итог - ничья")
    elif player_choice == "бумага" and comp_choice == "камень":
        messagebox.showinfo("Информация", f"Бумага бьёт камень. Вы победили победил.")
    elif player_choice == "бумага" and comp_choice == "ножницы":
        messagebox.showinfo("Информация", f"Ножницы режут бумагу. Вы победили.")

root = tk.Tk()
root.geometry("360x100")
root.title("Камень, ножницы, бумага")

button1 = ttk.Button(text="камень", width=8, command=game_button1)
button1.place(x = 2, y = 0)

button2 = ttk.Button(text="ножницы", width=8, command=game_button2)
button2.place(x = 120, y = 0)

button3 = ttk.Button(text="бумага", width=8, command=game_button3)
button3.place(x = 240, y=0)

root.mainloop()