# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:58:23 2026

@author: Anna Sarova
"""

"""
===========================================================
TIC TAC TOE GAME
===========================================================

Description:
This program is a simple Tic Tac Toe game made using
Python and Tkinter.

How to Play:
1. Player X goes first.
2. Click any square to place your mark.
3. Players take turns placing X and O.
4. Get 3 in a row to win.
5. If the board fills up with no winner,
   the game ends in a draw.
6. Press the Reset button to play again.

===========================================================
"""

import tkinter as tk
from tkinter import messagebox


class TicTacToeGame:
    # Handles the game logic.

    def __init__(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False

    def make_move(self, index):
        # Place the current player's symbol on the board.

        if self.board[index] == "" and not self.game_over:
            self.board[index] = self.current_player

            # Check for a winner
            if self.check_winner():
                self.game_over = True
                return f"Player {self.current_player} Wins!"

            # Check for draw
            if self.is_draw():
                self.game_over = True
                return "It's a Draw!"

            # Switch turns
            self.switch_player()

    def switch_player(self):
        # Switch between X and O.

        self.current_player = (
            "O" if self.current_player == "X" else "X"
        )

    def check_winner(self):
        # Check all winning combinations.

        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for combo in winning_combinations:
            a, b, c = combo

            if (
                self.board[a] == self.board[b] == self.board[c]
                and self.board[a] != ""
            ):
                return True

        return False

    def is_draw(self):
        # Check if all spaces are filled.

        return "" not in self.board

    def reset(self):
        # Reset the game board.

        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False


class TicTacToeGUI:
    # Handles the graphical interface.

    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x600")
        self.root.configure(bg="lightblue")

        # Create game object
        self.game = TicTacToeGame()

        # Title
        self.title_label = tk.Label(
            root,
            text="TIC TAC TOE",
            font=("Arial", 24, "bold"),
            bg="lightblue",
            fg="darkblue"
        )
        self.title_label.pack(pady=10)

        # Instructions for the player
        self.instructions = tk.Label(
            root,
            text="Click a square to place your mark.\nPlayer X starts first.",
            font=("Arial", 12),
            bg="lightblue"
        )
        self.instructions.pack()

        # Status label
        self.status_label = tk.Label(
            root,
            text="Player X's Turn",
            font=("Arial", 16, "bold"),
            bg="lightblue",
            fg="green"
        )
        self.status_label.pack(pady=10)

        # Frame to hold game buttons
        self.board_frame = tk.Frame(root, bg="black")
        self.board_frame.pack()

        self.buttons = []

        # Create 9 board buttons
        for i in range(9):

            button = tk.Button(
                self.board_frame,
                text="",
                font=("Arial", 24, "bold"),
                width=5,
                height=2,
                bg="white",
                command=self.create_button_command(i)
            )

            button.grid(
                row=i // 3,
                column=i % 3,
                padx=1,
                pady=1
            )

            self.buttons.append(button)

        # Reset button
        self.reset_button = tk.Button(
            root,
            text="Reset Game",
            font=("Arial", 14, "bold"),
            bg="orange",
            command=self.reset_game
        )

        self.reset_button.pack(pady=20)
    
    def create_button_command(self, index):
        def button_command():
            self.on_button_click(index)

        return button_command

    def on_button_click(self, index):
        # Handle player clicking a square.

        if self.game.board[index] == "" and not self.game.game_over:

            # Show player's mark
            self.buttons[index].config(
                text=self.game.current_player
            )

            # Run game logic
            result = self.game.make_move(index)

            # If game is over
            if result:

                self.status_label.config(text=result)

                messagebox.showinfo(
                    "Game Over",
                    result
                )

            else:
                # Update turn label
                self.status_label.config(
                    text=f"Player {self.game.current_player}'s Turn"
                )

    def reset_game(self):
        # Reset GUI and game logic.

        self.game.reset()

        for button in self.buttons:
            button.config(text="")

        self.status_label.config(
            text="Player X's Turn"
        )

# Run the game
def main():
    root = tk.Tk()
    game_gui = TicTacToeGUI(root)
    
    root.mainloop()

main()