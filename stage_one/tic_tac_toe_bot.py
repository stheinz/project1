import random

def print_board(board):
    """Druckt das Tic-Tac-Toe-Spielbrett."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Überprüft, ob ein Spieler gewonnen hat."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def user_move(board):
    """Lässt den Benutzer einen Zug machen."""
    while True:
        try:
            row, col = map(int, input("Geben Sie Zeile und Spalte (0-2) für Ihren Zug ein (z.B. 1 2): ").split())
            if board[row][col] == ' ':
                return row, col
            else:
                print("Ungültiger Zug. Das Feld ist bereits belegt.")
        except ValueError:
            print("Ungültige Eingabe. Geben Sie Zeile und Spalte als Zahlen ein.")
        except IndexError:
            print("Ungültige Zeile oder Spalte. Geben Sie Werte zwischen 0 und 2 ein.")

def bot_move(board):
    """Lässt den Bot einen Zug machen."""
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(available_moves)

def play_game():
    """Startet ein neues Spiel."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Willkommen beim Tic-Tac-Toe Chatbot-Spiel!")
    print_board(board)
    while True:
        # Benutzerzug
        user_row, user_col = user_move(board)
        board[user_row][user_col] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("Glückwunsch! Sie haben gewonnen!")
            break
        elif ' ' not in [cell for row in board for cell in row]:
            print("Unentschieden!")
            break
        # Botzug
        print("Der Bot denkt...")
        bot_row, bot_col = bot_move(board)
        board[bot_row][bot_col] = 'O'
        print_board(board)
        if check_winner(board, 'O'):
            print("Der Bot hat gewonnen!")
            break

if __name__ == "__main__":
    play_game()
