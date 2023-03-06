import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Create the grid of buttons
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 50), width=2, height=1,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
        
    def start(self):
        self.root.mainloop()
        
    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            winner = self.check_win()
            if winner:
                if winner == "tie":
                    tk.messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                else:
                    tk.messagebox.showinfo("Tic Tac Toe", f"Player {winner} has won the game!")
                self.root.destroy()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_win(self):
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != " ":
                return self.board[i][0]
            # Check columns
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != " ":
                return self.board[0][i]
            # Check diagonals
            elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
                return self.board[0][0]
            elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
                return self.board[0][2]
            # Check for tie
            elif " " not in self.board[0] and " " not in self.board[1] and " " not in self.board[2]:
                return "tie"
            else:
                return None

# Start the game
game = TicTacToe()
game.start()
