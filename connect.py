import tkinter as tk
import random

# Constants
ROWS = 6
COLS = 7
RADIUS = 30
PADDING = 10
WIDTH = COLS * (2 * RADIUS + PADDING)
HEIGHT = ROWS * (2 * RADIUS + PADDING)

board = [['' for _ in range(COLS)] for _ in range(ROWS)]
current_player = 'red'
game_over = False
game_mode = None  # 'PvP' or 'PvC'

def draw_board(canvas):
    for row in range(ROWS):
        for col in range(COLS):
            x = col * (2 * RADIUS + PADDING) + RADIUS + PADDING
            y = row * (2 * RADIUS + PADDING) + RADIUS + PADDING
            canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, fill='white', outline='blue', width=2)

def check_win(player):
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True
    return False

def display_message(message, color):
    canvas.create_rectangle(0, HEIGHT // 2 - 40, WIDTH, HEIGHT // 2 + 40, fill='black', outline='')
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text=message, fill=color,
                       font=('Arial', 28, 'bold'), justify='center')
    play_again_btn.pack(pady=10)

def computer_move():
    global current_player, game_over
    if game_over:
        return
    available_cols = [c for c in range(COLS) if board[0][c] == '']
    if not available_cols:
        return
    col = random.choice(available_cols)
    for row in reversed(range(ROWS)):
        if board[row][col] == '':
            board[row][col] = current_player
            x = col * (2 * RADIUS + PADDING) + RADIUS + PADDING
            y = row * (2 * RADIUS + PADDING) + RADIUS + PADDING
            canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS,
                               fill=current_player, outline='blue', width=2)

            if check_win(current_player):
                game_over = True
                display_message(f"{current_player.capitalize()} wins!", current_player)
                return

            if all(board[r][c] != '' for r in range(ROWS) for c in range(COLS)):
                game_over = True
                display_message("It's a draw!", 'white')
                return

            current_player = 'yellow' if current_player == 'red' else 'red'
            break

def drop_disc(event):
    global current_player, game_over
    if game_over or game_mode is None:
        return

    col = event.x // (2 * RADIUS + PADDING)
    if col < 0 or col >= COLS:
        return

    for row in reversed(range(ROWS)):
        if board[row][col] == '':
            board[row][col] = current_player
            x = col * (2 * RADIUS + PADDING) + RADIUS + PADDING
            y = row * (2 * RADIUS + PADDING) + RADIUS + PADDING
            canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS,
                               fill=current_player, outline='blue', width=2)

            if check_win(current_player):
                game_over = True
                display_message(f"{current_player.capitalize()} wins!", current_player)
                return

            if all(board[r][c] != '' for r in range(ROWS) for c in range(COLS)):
                game_over = True
                display_message("It's a draw!", 'white')
                return

            current_player = 'yellow' if current_player == 'red' else 'red'
            break

    if game_mode == 'PvC' and not game_over and current_player == 'yellow':
        canvas.after(500, computer_move)

def reset_game():
    global board, current_player, game_over
    canvas.delete("all")
    board = [['' for _ in range(COLS)] for _ in range(ROWS)]
    current_player = 'red'
    game_over = False
    draw_board(canvas)
    play_again_btn.pack_forget()

def set_mode(mode):
    global game_mode
    game_mode = mode
    mode_frame.pack_forget()       # Hide mode selection
    canvas.pack()                  # Show canvas
    draw_board(canvas)

# Tkinter UI
root = tk.Tk()
root.title("Connect Four")

# Mode selection screen
mode_frame = tk.Frame(root, bg='lightblue')
mode_frame.config(width=WIDTH, height=HEIGHT)
mode_frame.pack_propagate(False)
mode_frame.pack()


welcome_label = tk.Label(mode_frame, text="🎮 Select Game Mode", font=('Arial', 24, 'bold'), bg='lightblue')
welcome_label.pack(pady=20)

pvp_btn = tk.Button(mode_frame, text="Player vs Player", font=('Arial', 30), bg='black', fg='white',
                    width=20, command=lambda: set_mode('PvP'))
pvp_btn.pack(pady=10)

pvc_btn = tk.Button(mode_frame, text="Player vs Computer", font=('Arial', 30), bg='black', fg='white',
                    width=20, command=lambda: set_mode('PvC'))
pvc_btn.pack(pady=10)

# Game canvas (initially hidden)
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='blue')
canvas.bind("<Button-1>", drop_disc)

# Play Again button
play_again_btn = tk.Button(root, text="Play Again", font=('Arial', 14, 'bold'),
                           bg='black', fg='white', command=reset_game)

root.mainloop()


