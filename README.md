# TicTacToe

Tic-Tac-Toe ist ein beliebtes Spiel, das normalerweise auf einem 3x3-Raster gespielt wird. Zwei Spieler, oft als "X" und "O" bezeichnet, wechseln sich ab, ihre Symbole in leere Felder des Rasters zu setzen. Das Ziel ist es, drei Symbole in einer Reihe, Spalte oder Diagonale zu platzieren.

## Projektziel

Das Ziel meines Projektes ist es, ein interaktives Tic-Tac-Toe-Spiel zu entwickeln, bei dem ein Spieler gegen einen Computer-Bot antritt. Innerhalb des Projektes werden verschiedene Ansätze zur Schwierigkeit des Bots implementiert und die Interaktion mit dem Spiel erfolgt teils durch die Konsole und teils über eine GUI mithilfe von tkinter. Für den Lernfortschritt mithilfe des Reinforcement Learnings werden Plots zur Auswertung genommen.

## Ordnerstruktur

Das Projekt ist in verschiedene Stufen unterteilt, die jeweils durch eigene Ordner repräsentiert werden:

1. **Stage 1: Dumb Bot**
    - **Ordner:** `stage_one`
    - **Beschreibung:** In dieser Stufe macht der Computer-Bot zufällige Züge, ohne eine Strategie zu verfolgen.
    - **Nutzung:** Das Spiel kann über die Konsole gestartet werden.

2. **Stage 2: Minimax Algorithmus**
    - **Ordner:** `stage_two`
    - **Beschreibung:** In dieser Stufe verwendet der Computer-Bot den Minimax-Algorithmus, um den besten Zug zu finden, basierend auf einer vollständigen Suche des Spielbaums.
    - **Nutzung:** Das Spiel kann über die Konsole gestartet werden.

3. **Stage 3: Minimax Algorithmus mit Zufallsfaktor**
    - **Ordner:** `stage_three`
    - **Beschreibung:** Der Minimax-Algorithmus wird mit einem Zufallsfaktor erweitert, um die Vorhersagbarkeit des Bots zu verringern und seine Anpassungsfähigkeit zu verbessern.
    - **Nutzung:** Das Spiel kann über die Konsole gestartet werden.

4. **Stage 4: Reinforcement Learning**
    - **Ordner:** `stage_four`
    - **Beschreibung:** In dieser Stufe wird der Computer-Bot mithilfe von Deep Learning trainiert, um aus Datenmengen zu lernen und eine effektive Strategie zu entwickeln.
    - **Nutzung:** Das Spiel wird über eine GUI gestartet, die die Interaktion mit dem Benutzer ermöglicht.

## Spielablauf

Das Spiel beginnt mit einem leeren Spielfeld. Der menschliche Spieler macht seinen Zug, indem er eine Zelle auswählt. Danach macht der Computer seinen Zug. Die Züge werden abwechselnd gemacht, bis entweder ein Spieler gewinnt oder das Spielfeld voll ist (Unentschieden).

## Gewinnüberprüfung

Nach jedem Zug überprüft der Code, ob einer der Spieler gewonnen hat. Dies geschieht durch Überprüfung aller Reihen, Spalten und Diagonalen auf das Vorhandensein von drei übereinstimmenden Symbolen des Spielers.
