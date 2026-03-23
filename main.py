import tkinter as tk
import math

# Create window
root = tk.Tk()
root.title("AI Tic Tac Toe")

board = [" " for _ in range(9)]
buttons = []
player_score = 0
ai_score = 0

# Title
title = tk.Label(root, text="Tic Tac Toe - AI", font=("Arial", 18, "bold"))
title.grid(row=0, column=0, columnspan=3, pady=10)

# Winner check with highlight
def winner(b, p):
    win = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == p:
            for i in combo:
                buttons[i].config(bg="lightgreen")
            return True
    return False

# Check draw
def draw(b):
    return " " not in b

# Minimax algorithm
def minimax(b, is_max):
    if winner(b, "O"):
        return 1
    if winner(b, "X"):
        return -1
    if draw(b):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = " "
                best = min(best, score)
        return best

# AI move
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    if move != -1:
        board[move] = "O"
        buttons[move]["text"] = "O"
        buttons[move].config(fg="red")

# Button click
def click(i):
    global player_score, ai_score

    if board[i] == " ":
        board[i] = "X"
        buttons[i]["text"] = "X"
        buttons[i].config(fg="blue")

        if winner(board, "X"):
            player_score += 1
            result_label.config(text="You Win!")
            update_score()
            disable_buttons()
            return

        if draw(board):
            result_label.config(text="Draw!")
            return

        ai_move()

        if winner(board, "O"):
            ai_score += 1
            result_label.config(text="Computer Wins!")
            update_score()
            disable_buttons()
            return

        if draw(board):
            result_label.config(text="Draw!")

# Disable buttons
def disable_buttons():
    for b in buttons:
        b.config(state="disabled")

# Restart game
def restart():
    global board
    board = [" " for _ in range(9)]
    for b in buttons:
        b.config(text=" ", state="normal", fg="black", bg="SystemButtonFace")
    result_label.config(text="Your Turn")

# Update score
def update_score():
    score_label.config(text=f"Player: {player_score}  AI: {ai_score}")

# Create buttons
for i in range(9):
    btn = tk.Button(root, text=" ", font=("Arial", 20),
                    width=5, height=2,
                    command=lambda i=i: click(i))
    btn.grid(row=(i//3)+1, column=i%3)
    buttons.append(btn)

# Result label
result_label = tk.Label(root, text="Your Turn", font=("Arial", 14))
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# Score label
score_label = tk.Label(root, text="Player: 0  AI: 0", font=("Arial", 12))
score_label.grid(row=5, column=0, columnspan=3)

# Restart button
tk.Button(root, text="Restart", command=restart).grid(row=6, column=0, columnspan=3, pady=10)

# Run app
root.mainloop()
