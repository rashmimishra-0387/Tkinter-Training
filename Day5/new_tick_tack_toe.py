import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root, mode="multiplayer"):
        self.root = root
        self.mode = mode
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0}
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
    
    def create_widgets(self):
        self.score_label = tk.Label(self.root, text=self.get_score_text(), font=('normal', 12))
        self.score_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row + 1, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        #self.buttons[row][col]['text']: Checks if the button is empty before making a move.
        #self.check_winner(): Checks if the current move resulted in a win.-
        if self.buttons[row][col]['text'] == "" and not self.check_winner():
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.update_score(self.current_player)
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                if self.mode == "single" and self.current_player == "X":
                    self.current_player = "O"
                    self.ai_move()
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"
    
    def ai_move(self):
        empty_buttons = [(r, c) for r in range(3) for c in range(3) if self.buttons[r][c]['text'] == ""]
        if empty_buttons:
            r, c = random.choice(empty_buttons)
            self.buttons[r][c]['text'] = "O"
            if self.check_winner():
                messagebox.showinfo("Game Over", "Player O wins!")
                self.update_score("O")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "X"

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                return True
        for col in range(3):
            if self.buttons[0][col]['text'] == self.buttons[1][col]['text'] == self.buttons[2][col]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def is_board_full(self):
        return all(self.buttons[row][col]['text'] != "" for row in range(3) for col in range(3))

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]['text'] = ""
        self.current_player = "X"
        self.update_score_label()

    def update_score(self, player):
        self.scores[player] += 1

    def update_score_label(self):
        self.score_label.config(text=self.get_score_text())

    def get_score_text(self):
        return f"Score - X: {self.scores['X']} | O: {self.scores['O']}"

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe Menu")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select Mode", font=('normal', 20)).pack(pady=20)
        tk.Button(self.root, text="Single Player", font=('normal', 15), command=self.start_single_player).pack(pady=10)
        tk.Button(self.root, text="Multiplayer", font=('normal', 15), command=self.start_multiplayer).pack(pady=10)

    def start_single_player(self):
        self.root.destroy()
        self.start_game("single")

    def start_multiplayer(self):
        self.root.destroy()
        self.start_game("multiplayer")

    def start_game(self, mode):
        root = tk.Tk()
        TicTacToe(root, mode)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    Menu(root)
    root.mainloop()