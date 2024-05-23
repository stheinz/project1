"""Für diese Datei wurde ChatGPT als Hilfsmittel verwendet"""
import numpy as np
import matplotlib.pyplot as plt
import random

# Definiere die Spieler
HUMAN = 'X'
COMPUTER = 'O'
EMPTY = ' '

# Definiere Q-Learning Parameter
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
EPSILON = 0.1


class TicTacToeRL:
    def __init__(self):
        self.q_values = {}  # Dictionary zum Speichern der Q-Werte

    def get_state_hash(self, board):
        """Erzeugt einen Hash-Wert für den aktuellen Zustand des Spielfelds."""
        return str(np.array(board).reshape(9))

    def q_learning(self, board, epsilon=EPSILON):
        """Führt einen Q-Learning-Schritt für den aktuellen Zustand des Spielfelds durch."""
        state = self.get_state_hash(board)
        if state not in self.q_values:
            self.q_values[state] = {}
        if np.random.rand() < epsilon:
            # Wähle einen zufälligen Zug
            available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
            if not available_moves:
                return random.choice([(i, j) for i in range(3) for j in range(3)])
            action = random.choice(available_moves)
        else:
            # Wähle den Zug mit dem höchsten Q-Wert
            max_q_value = float('-inf')
            best_action = None
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        next_state = self.get_state_hash(board)
                        q_value = self.q_values[state].get((i, j), 0)
                        if q_value > max_q_value:
                            max_q_value = q_value
                            best_action = (i, j)
            if best_action is None:
                return random.choice([(i, j) for i in range(3) for j in range(3)])
            action = best_action
        return action

    def update_q_values(self, state, action, reward, next_state):
        """Aktualisiert die Q-Werte basierend auf dem erhaltenen Reward."""
        if state not in self.q_values:
            self.q_values[state] = {}
        if next_state not in self.q_values:
            self.q_values[next_state] = {}
        current_q_value = self.q_values[state].get(action, 0)
        max_next_q_value = max(self.q_values[next_state].values(), default=0)
        self.q_values[state][action] = current_q_value + LEARNING_RATE * (
                    reward + DISCOUNT_FACTOR * max_next_q_value - current_q_value)

    def play_game(self):
        """Spielt ein Spiel Tic-Tac-Toe zwischen dem Computer und sich selbst."""
        board = [[EMPTY for _ in range(3)] for _ in range(3)]
        states = []
        while True:
            # Computerzug
            state = self.get_state_hash(board)
            action = self.q_learning(board)
            states.append(state)
            row, col = action
            board[row][col] = COMPUTER
            if self.check_winner(board, COMPUTER):
                # Belohnung für den Computer, wenn er gewinnt
                self.update_q_values(states[-1], action, 1, self.get_state_hash(board))
                break
            elif self.is_board_full(board):
                # Belohnung für Unentschieden
                self.update_q_values(states[-1], action, 0, self.get_state_hash(board))
                break
            # Menschlicher Zug
            row, col = random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY])
            board[row][col] = HUMAN
            if self.check_winner(board, HUMAN):
                # Bestrafung für den Computer, wenn der Mensch gewinnt
                self.update_q_values(states[-1], action, -1, self.get_state_hash(board))
                break
        return states

    def check_winner(self, board, player):
        """Überprüft, ob ein Spieler gewonnen hat."""
        lines = [[(i, j) for j in range(3)] for i in range(3)] + \
                [[(i, j) for i in range(3)] for j in range(3)] + \
                [[(i, i) for i in range(3)]] + \
                [[(i, 2 - i) for i in range(3)]]
        for line in lines:
            if all(board[i][j] == player for i, j in line):
                return True
        return False

    def is_board_full(self, board):
        """Überprüft, ob das Spielfeld voll ist."""
        return all(board[i][j] != EMPTY for i in range(3) for j in range(3))


def plot_learning_progress(states):
    """Plottet den Lernfortschritt des Computers."""
    num_states = len(states)
    computer_moves = [state.count(COMPUTER) for state in states]
    avg_computer_moves = [sum(computer_moves[:i + 1]) / (i + 1) for i in range(num_states)]
    plt.plot(range(num_states), avg_computer_moves, color='blue', linewidth=2)
    plt.xlabel('Spielnummer')
    plt.ylabel('Durchschnittliche Anzahl der Computer-Züge')
    plt.title('Lernfortschritt des Computers')
    plt.xlim(0, 500)  # Nur die ersten 500 Spielnummern anzeigen
    plt.ylim(0, max(avg_computer_moves) * 1.1)  # Dynamische y-Grenze
    plt.grid(True)
    plt.show()


def main():
    rl_agent = TicTacToeRL()
    num_games = 2000
    all_states = []
    for _ in range(num_games):
        states = rl_agent.play_game()
        all_states.extend(states)
    plot_learning_progress(all_states)


if __name__ == "__main__":
    main()
