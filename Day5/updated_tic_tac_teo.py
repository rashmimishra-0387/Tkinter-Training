import tkinter as tk
from tkinter import messagebox
import random

# Global variables
current_player = "X"
scores = {"X": 0, "O": 0}
buttons = [[None for i in range(3)] for j in range(3)]
mode = "multiplayer"  # default mode

def create_widgets(root):
    global score_label
    score_label = tk.Label(root, text=get_score_text(), font=('normal', 12))
    score_label.grid(row=0, column=0, columnspan=3, pady=10)
    
    for row in range(3):
        for col in range(3):
            button_widget = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                                      command=lambda r=row, c=col: on_button_click(r, c, root))
            button_widget.grid(row=row + 1, column=col)
            buttons[row][col] = button_widget

def on_button_click(row, col, root):
    global current_player
    if buttons[row][col]['text'] == "" and not check_winner():
        buttons[row][col]['text'] = current_player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            update_score(current_player)
            reset_game(root)
        elif is_board_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game(root)
        else:
            if mode == "single" and current_player == "X":
                current_player = "O"
                ai_move(root)
            else:
                current_player = "O" if current_player == "X" else "X"

def ai_move(root):
    empty_buttons = [(r, c) for r in range(3) for c in range(3) if buttons[r][c]['text'] == ""]
    if empty_buttons:
        r, c = random.choice(empty_buttons)
        buttons[r][c]['text'] = "O"
        if check_winner():
            messagebox.showinfo("Game Over", "Player O wins!")
            update_score("O")
            reset_game(root)
        elif is_board_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game(root)
        else:
            global current_player
            current_player = "X"

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    return False

def is_board_full():
    return all(buttons[row][col]['text'] != "" for row in range(3) for col in range(3))

def reset_game(root):
    global current_player
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ""
    current_player = "X"
    update_score_label()

def update_score(player):
    scores[player] += 1

def update_score_label():
    score_label.config(text=get_score_text())

def get_score_text():
    return f"Score - X: {scores['X']} | O: {scores['O']}"

def start_single_player():
    global mode
    mode = "single"
    start_game()

def start_multiplayer():
    global mode
    mode = "multiplayer"
    start_game()

def start_game():
    root = tk.Tk()
    create_widgets(root)
    root.mainloop()

def create_menu():
    menu_root = tk.Tk()
    menu_root.title("Tic Tac Toe Menu")
    
    tk.Label(menu_root, text="Select Mode", font=('normal', 20)).pack(pady=20)
    tk.Button(menu_root, text="Single Player", font=('normal', 15), command=start_single_player).pack(pady=10)
    tk.Button(menu_root, text="Multiplayer", font=('normal', 15), command=start_multiplayer).pack(pady=10)
    
    menu_root.mainloop()


create_menu()
