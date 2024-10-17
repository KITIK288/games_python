import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Угадай число")

        self.secret_number = random.randint(1, 10)
        self.attempts = 0

        self.label = tk.Label(master, text="Угадайте число от 1 до 10:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Угадать", command=self.check_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.reset_button = tk.Button(master, text="Сбросить", command=self.reset_game)
        self.reset_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess == 1:
                attempt = "попытку"

            if guess < self.secret_number:
                self.result_label.config(text="Ваше число меньше загаданного компьютером. Попробуйте снова.")
            elif guess > self.secret_number:
                self.result_label.config(text="Ваше число больше загаданного компьютером. Попробуйте снова.")
            else:
                self.result_label.config(text=f"Поздравляем! Вы угадали число {self.secret_number} за {self.attempts} попыток.")
        except ValueError:
            self.result_label.config(text="Пожалуйста, введите коректное число.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
