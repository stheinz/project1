# TicTacToe

1. Tic-Tac-Toe:
    Tic-Tac-Toe ist ein beliebtes Spiel, das normalerweise auf einem 3x3-Raster gespielt wird.
    Zwei Spieler, oft als "X" und "O" bezeichnet, wechseln sich ab, um ihre Symbole in leere Felder        des Rasters zu setzen.
    Das Ziel ist es, drei Symbole in einer Reihe, Spalte oder Diagonale zu platzieren.

2. Der Code:
    Der bereitgestellte Code ist eine Python-Implementierung des Tic-Tac-Toe-Spiels.
    Es gibt eine Funktion play_game(), die das Spiel steuert.
    Das Spielbrett wird als 3x3-Liste repräsentiert, und die Spieler sind als 'X' (der menschliche         Spieler) und 'O' (der Computer) definiert.

3. Spielablauf:
    Das Spiel beginnt mit einem leeren Spielbrett.
    Der menschliche Spieler macht seinen Zug, indem er die Zeile und Spalte seines Zuges eingibt.
    Dann macht der Computer seinen Zug.
    Die Züge werden abwechselnd gemacht, bis entweder ein Spieler gewinnt oder das Spiel unentschieden     endet.

4. Gewinnüberprüfung:
    Nach jedem Zug überprüft der Code, ob einer der Spieler gewonnen hat.
    Dies geschieht durch Überprüfung aller Reihen, Spalten und Diagonalen auf das Vorhandensein von        drei aufeinanderfolgenden Symbolen des gleichen Spielers.

5. Minimax-Algorithmus:
    Um den besten Zug für den Computer zu finden, wird der Minimax-Algorithmus verwendet.
    Dies ist ein algorithmisches Konzept, das darauf abzielt, die bestmöglichen Züge für beide Spieler     zu berechnen, unter der Annahme, dass der Gegner ebenfalls optimal spielt.
    Der Algorithmus verwendet rekursive Suche und Bewertung, um den besten Zug zu finden.

6. Zufälliger Zug:
    Um das Spiel interessanter zu gestalten, gibt es eine zufällige Komponente im Code.
    Manchmal, wenn der Computer seinen Zug macht, entscheidet er sich zufällig für einen Zug anstatt       den besten Zug zu berechnen.
    Dies fügt dem Spiel eine gewisse Unvorhersehbarkeit hinzu. -> tic_tac_toe_interesting.py