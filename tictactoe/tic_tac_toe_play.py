import tkinter as tk
from tkinter import messagebox
from tic_tac_toe_reinforcement import TicTacToeRL, COMPUTER, HUMAN, EMPTY

class TicTacToeUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.rl_agent = TicTacToeRL()
        self.board_buttons = []
        self.bot_moves = 0  # Variable zur Zählung der Bot-Züge
        self.create_board()

    def create_board(self):
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.master, text="", width=10, height=5,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.board_buttons.append(row_buttons)

    def on_click(self, row, col):
        if self.board_buttons[row][col]["text"] == "":
            # Menschlicher Zug
            self.board_buttons[row][col]["text"] = HUMAN
            if self.check_winner(HUMAN):
                self.show_message("Herzlichen Glückwunsch! Sie haben gewonnen!")
                self.show_final_board()
                self.restart()
                return
            elif self.is_board_full():
                self.show_message("Unentschieden!")
                self.show_final_board()
                self.restart()
                return

            # Überprüfen, ob das Spiel noch nicht beendet ist
            if not self.is_board_full():
                # Computerzug
                while True:
                    computer_row, computer_col = self.rl_agent.q_learning(self.get_board_state())
                    if self.board_buttons[computer_row][computer_col]["text"] == "":
                        self.board_buttons[computer_row][computer_col]["text"] = COMPUTER
                        break

                if self.check_winner(COMPUTER):
                    self.show_message("Der Computer hat gewonnen!")
                    self.show_final_board()
                    self.restart()
                    return
                elif self.is_board_full():
                    self.show_message("Unentschieden!")
                    self.show_final_board()
                    self.restart()
                    return

    def show_final_board(self):
        board_str = ""
        for i in range(3):
            for j in range(3):
                cell_value = self.board_buttons[i][j]["text"]
                if cell_value == "":
                    cell_value = "-"
                board_str += cell_value + " "
            board_str += "\n"
        self.show_message("Endgültiges Spielfeld:\n" + board_str)

    def check_winner(self, player):
        """Überprüft, ob ein Spieler gewonnen hat."""
        # Überprüfen der Zeilen und Spalten
        for i in range(3):
            if all(self.board_buttons[i][j]["text"] == player for j in range(3)):
                return True
            if all(self.board_buttons[j][i]["text"] == player for j in range(3)):
                return True
        # Überprüfen der Diagonalen
        if all(self.board_buttons[i][i]["text"] == player for i in range(3)) or \
                all(self.board_buttons[i][2 - i]["text"] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        # Überprüfen, ob das Spielfeld voll ist
        return all(self.board_buttons[i][j]["text"] in [HUMAN, COMPUTER] for i in range(3) for j in range(3))

    def get_board_state(self):
        # Rückgabe des aktuellen Spielfeldzustands als Liste oder Array
        return [[self.board_buttons[i][j]["text"] for j in range(3)] for i in range(3)]

    def show_message(self, message):
        messagebox.showinfo("Spiel beendet", message)

    def restart(self):
        # Setze das Spielfeld zurück
        for i in range(3):
            for j in range(3):
                self.board_buttons[i][j]["text"] = ""


def main():
    root = tk.Tk()
    tic_tac_toe_ui = TicTacToeUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
