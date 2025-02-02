from tkinter import *
import random
from tkinter import messagebox
import time

root = Tk()
root.title("Pong Game")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)

canvas = Canvas(root, width=600, height=500, bd=1, highlightthickness=1)
canvas.config(bg="black")
canvas.pack()

# Scoreboard text
score_text = canvas.create_text(300, 20, font=("Arial", 20, "bold"), text=" : ", fill="white")

root.update()
canvas.create_line(300, 0, 300, 600, fill="white")

# Ball properties
ball_x = 0
ball_y = 0
ball_dx = 0
ball_dy = 0
ball_speed = 4
ball_score1 = 0
ball_score2 = 0

# Paddle properties
paddle1_y = 0
paddle2_y = 0
paddle_speed = 4

# Initial positions
paddle1 = canvas.create_rectangle(10, 180, 25, 280, fill="orange")
paddle2 = canvas.create_rectangle(575, 180, 590, 280, fill="lightgreen")
ball = canvas.create_oval(10, 10, 30, 30, fill="yellow")

canvas.move(ball, 283, 300)

# Set random ball speed
starts = [-ball_speed, -ball_speed + 1, -ball_speed + 2, ball_speed - 1, ball_speed, ball_speed + 1]
random.shuffle(starts)
ball_dx = starts[1]
ball_dy = starts[2]

# Update the score display
def update_score():
    canvas.itemconfigure(score_text, text=f"{ball_score1} : {ball_score2}")

# Ball movement logic
def move_ball():
    global ball_dx, ball_dy, ball_score1, ball_score2

    # Move the ball
    canvas.move(ball, ball_dx, ball_dy)
    pos = canvas.coords(ball)

    # Ball collision with the top and bottom
    if pos[1] <= 0 or pos[3] >= canvas.winfo_height():
        ball_dy = -ball_dy

    # Ball collision with the left and right sides
    if pos[0] <= 0:
        ball_dx = -ball_dx
        ball_score2 += 1
        update_score()

    if pos[2] >= canvas.winfo_width():
        ball_dx = -ball_dx
        ball_score1 += 1
        update_score()

    # Ball collision with paddles
    if hit_paddle(paddle1, pos):
        ball_dx = ball_speed
    if hit_paddle(paddle2, pos):
        ball_dx = -ball_speed

# Paddle movement logic
def move_paddle1(event):
    global paddle1_y
    if event.keysym == 'a':
        paddle1_y = -paddle_speed
    elif event.keysym == 'd':
        paddle1_y = paddle_speed

def move_paddle2(event):
    global paddle2_y
    if event.keysym == 'Left':
        paddle2_y = -paddle_speed
    elif event.keysym == 'Right':
        paddle2_y = paddle_speed

# Paddle boundary check
def move_paddle(paddle, y_move):
    canvas.move(paddle, 0, y_move)
    pos = canvas.coords(paddle)
    if pos[1] <= 0:
        y_move = 0
    if pos[3] >= canvas.winfo_height():
        y_move = 0
    return y_move

# Check if the ball hits the paddle
def hit_paddle(paddle, ball_pos):
    paddle_pos = canvas.coords(paddle)
    if ball_pos[1] >= paddle_pos[1] and ball_pos[1] <= paddle_pos[3]:
        if ball_pos[0] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
            return True
    return False

# Key bindings
canvas.bind_all('a', move_paddle1)
canvas.bind_all('d', move_paddle1)
canvas.bind_all('<KeyPress-Left>', move_paddle2)
canvas.bind_all('<KeyPress-Right>', move_paddle2)

# Main game loop
while True:
    if ball_score1 == 10 or ball_score2 == 10:
        messagebox.showinfo("Game Over", f"Player 1 = {ball_score1} Player 2 = {ball_score2}")
        break

    # Update game elements
    move_ball()
    paddle1_y = move_paddle(paddle1, paddle1_y)
    paddle2_y = move_paddle(paddle2, paddle2_y)

    # Draw elements
    canvas.move(paddle1, 0, paddle1_y)
    canvas.move(paddle2, 0, paddle2_y)

    root.update_idletasks()
    root.update()

    # Slow down the loop
    time.sleep(0.01)

root.mainloop()
