import tkinter as tk
import random


PLAYER_SYMBOL = "❌"
COMPUTER_SYMBOL = "🟡"


BG_COLOR = "#f7f7f7"
BTN_COLOR = "#ffffff"
WIN_COLOR = "#c8f7c5"
LOSE_COLOR = "#f7c5c5"
TIE_COLOR = "#f0e68c"


root = tk.Tk()
root.title("✨ Tic-Tac-Toe Almdrasa ✨")
root.configure(bg=BG_COLOR)


player_score = 0
computer_score = 0
buttons = [[None for _ in range(3)] for _ in range(3)]


score_label = tk.Label(root, text=f"You: {player_score}   Computer: {computer_score}",
                    font=('Arial', 16, 'bold'), bg=BG_COLOR, fg="#333")
score_label.grid(row=0, column=0, columnspan=3, pady=(10, 0))

result_label = tk.Label(root, text="", font=('Arial', 14), bg=BG_COLOR)
result_label.grid(row=1, column=0, columnspan=3, pady=5)

def update_score():
    score_label.config(text=f"You: {player_score}   Computer: {computer_score}")

def disable_all_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")

def enable_all_buttons():
    for row in buttons:
        for btn in row:
            btn.config(text="", bg=BTN_COLOR, state="normal")

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return buttons[i][0]['text'], [(i, 0), (i, 1), (i, 2)]
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return buttons[0][i]['text'], [(0, i), (1, i), (2, i)]
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text'], [(0, 0), (1, 1), (2, 2)]
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text'], [(0, 2), (1, 1), (2, 0)]
    if all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
        return "Tie", []
    return None, []

def highlight_cells(cells, color):
    for i, j in cells:
        buttons[i][j].config(bg=color)

def computer_move():
    empty = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]['text'] == ""]
    if empty:
        i, j = random.choice(empty)
        buttons[i][j].config(text=COMPUTER_SYMBOL)

def handle_result(winner, cells):
    global player_score, computer_score
    if winner == PLAYER_SYMBOL:
        player_score += 1
        result_label.config(text="🎉 You Win!")
        highlight_cells(cells, WIN_COLOR)
    elif winner == COMPUTER_SYMBOL:
        computer_score += 1
        result_label.config(text="💻 Computer Wins!")
        highlight_cells(cells, LOSE_COLOR)
    elif winner == "Tie":
        result_label.config(text="🤝 It's a Tie!")
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(bg=TIE_COLOR)
    update_score()
    disable_all_buttons()

def computer_turn_after_player():
    computer_move()
    winner, cells = check_winner()
    if winner:
        handle_result(winner, cells)

def on_click(i, j):
    if buttons[i][j]['text'] == "":
        buttons[i][j].config(text=PLAYER_SYMBOL)
        winner, cells = check_winner()
        if winner:
            handle_result(winner, cells)
            return
        root.after(600, computer_turn_after_player) 

def restart_game():
    enable_all_buttons()
    result_label.config(text="")


restart_button = tk.Button(root, text="🔁 Restart", font=('Arial', 13), bg="#ddd", command=restart_game)
restart_button.grid(row=2, column=1, pady=10)


for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", font=('Arial', 24), width=5, height=2,
                        bg=BTN_COLOR, command=lambda i=i, j=j: on_click(i, j))
        btn.grid(row=i + 3, column=j, padx=5, pady=5)
        buttons[i][j] = btn


root.mainloop()
