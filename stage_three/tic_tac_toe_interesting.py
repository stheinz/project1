import random

# Definiere die Spieler
HUMAN = 'X'
COMPUTER = 'O'


def print_board(board):
    """Druckt das Tic-Tac-Toe-Spielbrett."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def available_moves(board):
    """Gibt eine Liste der verfügbaren Züge zurück."""
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves


def check_winner(board, player):
    """Überprüft, ob ein Spieler gewonnen hat."""
    # Zeilen
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Spalten
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonale
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def evaluate(board):
    """Bewertet den Zustand des Bretts für den MiniMax-Algorithmus."""
    if check_winner(board, COMPUTER):
        return 1
    elif check_winner(board, HUMAN):
        return -1
    else:
        return 0


def minimax(board, depth, maximizing_player):
    """Minimax-Algorithmus zur Ermittlung des besten Zugs."""
    if check_winner(board, COMPUTER):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if not available_moves(board):
        return 0

    if maximizing_player: # bester Zug für den maximierenden Spieler (COM)
        max_eval = float('-inf') # hier wird die variable mit dem wert negativer Unendlichkeit initialisiert
        for move in available_moves(board):
            row, col = move
            board[row][col] = COMPUTER
            eval = minimax(board, depth + 1, False) # False damit klar ist, dass der Mensch der nächste Spieler ist
            board[row][col] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else: # bester Zug für den minimierender Spieler (Human)
        min_eval = float('inf')
        for move in available_moves(board):
            row, col = move
            board[row][col] = HUMAN
            eval = minimax(board, depth + 1, True)
            board[row][col] = ' '
            min_eval = min(min_eval, eval)
        return min_eval


def best_move(board, random_chance=0.1):
    """Gibt den besten Zug für den Computer zurück."""
    if random.random() < random_chance:
        return random.choice(available_moves(board))

    best_score = float('-inf')
    best_move = None
    for move in available_moves(board):
        row, col = move
        board[row][col] = COMPUTER
        score = minimax(board, 0, False)
        board[row][col] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def play_game():
    """Startet ein neues Spiel."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Willkommen beim Tic-Tac-Toe Chatbot-Spiel!")
    print_board(board)
    while True:
        # Benutzerzug
        row, col = map(int, input("Geben Sie Zeile und Spalte (0-2) für Ihren Zug ein (z.B. 1 2): ").split())
        if board[row][col] == ' ':
            board[row][col] = HUMAN
        else:
            print("Ungültiger Zug. Das Feld ist bereits belegt.")
            continue
        print_board(board)
        if check_winner(board, HUMAN):
            print("Herzlichen Glückwunsch! Sie haben gewonnen!")
            break
        elif ' ' not in [cell for row in board for cell in row]:
            print("Unentschieden!")
            break
        # Computerzug
        print("Der Bot macht seinen Zug")
        row, col = best_move(board)
        board[row][col] = COMPUTER
        print_board(board)
        if check_winner(board, COMPUTER):
            print("Der Bot hat gewonnen!")
            break


if __name__ == "__main__":
    play_game()