import tkinter as tk
from tkinter import messagebox
import random


window = tk.Tk()
window.title("Tic Tac Toe - Stylish Edition")
window.geometry("800x600")
window.configure(bg="#121212")  


# Variables
current_player = "X"
board = [["" for _ in range(4)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
mode = None

# Winner check
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    for row in board:
        for cell in row:
            if cell == "":
                return None
    return "Draw"


def reset_board():
    global board, current_player, turn_label
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal", bg="#1f1f1f", fg="white")
    turn_label.config(text="Player X's Turn")



def end_game(result):
    overlay = tk.Frame(window, bg="#000000", width=window.winfo_width(), height=window.winfo_height())
    overlay.place(relx=0.5, rely=0.5, anchor="center")

    message = "It's a Draw!" if result == "Draw" else f"🎉 Player {result} Wins! 🎉"

    msg_label = tk.Label(overlay, text=message, font=("Arial", 50, "bold"), fg="#ffffff", bg="#000000")
    msg_label.pack(pady=40)

    btn_frame = tk.Frame(overlay, bg="#000000")
    btn_frame.pack()

    tk.Button(btn_frame, text=" Play Again", font=("Arial", 18), bg="#4caf50", fg="white",
              command=lambda: [overlay.destroy(), reset_board()]).pack(side="left", padx=20)

    tk.Button(btn_frame, text=" Main Menu", font=("Arial", 18), bg="#2196f3", fg="white",
              command=lambda: [overlay.destroy(), game_frame.pack_forget(), mode_frame.pack(expand=True)]).pack(side="left", padx=20)



def computer_move():
    global current_player
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    if empty:
        i, j = random.choice(empty)
        board[i][j] = "O"
        buttons[i][j].config(text="O", state="disabled", bg="#ff4d4d", fg="white")
        result = check_winner()
        if result:
            end_game(result)
        else:
            current_player = "X"


def on_click(i, j):
    global current_player, turn_label
    if board[i][j] == "":
        board[i][j] = current_player
        color = "#4d94ff" if current_player == "X" else "#ff4d4d"
        buttons[i][j].config(text=current_player, state="disabled", bg=color, fg="white")
        result = check_winner()
        if result:
            end_game(result)
        else:
            if mode == "PvP":
                current_player = "O" if current_player == "X" else "X"
                turn_label.config(text=f"Player {current_player}'s Turn")
            elif mode == "PvC":
                if current_player == "X":
                    current_player = "O"
                    turn_label.config(text="Computer's Turn")
                    window.after(300, computer_move)


# Mode selection handler
def start_game(selected_mode):
    global mode
    mode = selected_mode
    mode_frame.pack_forget()
    game_frame.pack(expand=True)

# UI Setup
mode_frame = tk.Frame(window, bg="#121212")
tk.Label(mode_frame, text="Select Game Mode", font=("Arial", 28), fg="white", bg="#121212").pack(pady=30)
tk.Button(mode_frame, text="Player vs Player", font=("Arial", 18), width=25, bg="#4caf50", fg="white",
          command=lambda: start_game("PvP")).pack(pady=15)
tk.Button(mode_frame, text="Player vs Computer", font=("Arial", 18), width=25, bg="#2196f3", fg="white",
          command=lambda: start_game("PvC")).pack(pady=15)
tk.Button(mode_frame, text="Exit", font=("Arial", 16), width=15, bg="#f44336", fg="white",
          command=window.destroy).pack(pady=40)
mode_frame.pack(expand=True)

# Game Frame
game_frame = tk.Frame(window, bg="#121212")
# Add Turn Label
turn_label = tk.Label(game_frame, text="Player X's Turn", font=("Arial", 24),
                      fg="white", bg="#121212")
turn_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))


for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(game_frame, text="", font=("Arial", 40), width=5, height=2,
                                  bg="#1f1f1f", fg="white",
                                  command=lambda r=i, c=j: on_click(r, c))
        buttons[i][j].grid(row=i+1, column=j, padx=10, pady=10)

# Restart & Exit buttons
tk.Button(game_frame, text="Restart", font=("Arial", 16), bg="#ff9800", fg="white",
          command=reset_board).grid(row=4, column=0, columnspan=1, pady=20)

tk.Button(game_frame, text="Main Menu", font=("Arial", 16), bg="#9c27b0", fg="white",
          command=lambda: [game_frame.pack_forget(), mode_frame.pack(expand=True)]).grid(row=4, column=1, columnspan=1, pady=20)

tk.Button(game_frame, text="Exit", font=("Arial", 16), bg="#e91e63", fg="white",
          command=window.destroy).grid(row=4, column=2, columnspan=1, pady=20)

window.mainloop()
