import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - Alternate Version")
        self.window.geometry("310x370")
        self.window.resizable(False, False)
        
        self.current_player = "X"
        self.board = [""] * 9
        
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        self.status = tk.Label(self.window, text="Player X's Turn", font=('Arial', 14))
        self.status.pack(pady=10)

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.frame, text="", font=('Arial', 20), width=6, height=2,
                            command=lambda i=i: self.button_click(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def button_click(self, index):
        if self.buttons[index]["text"] == "":
            self.buttons[index]["text"] = self.current_player
            self.board[index] = self.current_player

            if self.check_winner(self.current_player):
                self.end_game(f"Player {self.current_player} wins!")
            elif "" not in self.board:
                self.end_game("It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self, player):
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in winning_combos:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def end_game(self, result):
        messagebox.showinfo("Game Over", result)
        self.reset_game()

    def reset_game(self):
        for btn in self.buttons:
            btn["text"] = ""
        self.board = [""] * 9
        self.current_player = "X"
        self.status.config(text="Player X's Turn")

if __name__ == "__main__":
    TicTacToeGame()
