import tkinter as tk
import random


root = tk.Tk()
root.title("Tic-Tac-Toe Almdrasa")


player_score = 0
computer_score = 0
buttons = [[None for _ in range(3)] for _ in range(3)]


score_label = tk.Label(root, text=f"You: {player_score}  Computer: {computer_score}", font=('Arial', 16))
score_label.grid(row=0, column=0, columnspan=3, pady=10)

result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.grid(row=1, column=0, columnspan=3)

def update_score():
    score_label.config(text=f"You: {player_score}  Computer: {computer_score}")

def disable_all_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")

def enable_all_buttons():
    for row in buttons:
        for btn in row:
            btn.config(text="", state="normal")

def check_winner():

    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return buttons[i][0]['text']
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return buttons[0][i]['text']
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text']
    

    if all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
        return "Tie"
    return None

def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]['text'] == ""]
    if empty_cells:
        i, j = random.choice(empty_cells)
        buttons[i][j].config(text="O")

def handle_result(winner):
    global player_score, computer_score
    if winner == "X":
        player_score += 1
        result_label.config(text="You Win!")
    elif winner == "O":
        computer_score += 1
        result_label.config(text="Computer Wins!")
    else:
        result_label.config(text="It's a Tie!")
    update_score()
    disable_all_buttons()

def computer_turn_after_player():
    computer_move()
    winner = check_winner()
    if winner:
        handle_result(winner)

def on_click(i, j):
    if buttons[i][j]['text'] == "":
        buttons[i][j].config(text="X")
        winner = check_winner()
        if winner:
            handle_result(winner)
            return

        root.after(400, computer_turn_after_player)

def restart_game():
    enable_all_buttons()
    result_label.config(text="")


restart_button = tk.Button(root, text="restart", font=('Arial', 14), command=restart_game)
restart_button.grid(row=2, column=1, pady=10)


for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="", font=('Arial', 24), width=6, height=3,
                        command=lambda i=i, j=j: on_click(i, j))
        button.grid(row=i + 3, column=j)
        buttons[i][j] = button


root.mainloop()
