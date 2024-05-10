# max_eval = float('-inf')
* In der Zeile max_eval = float('-inf') wird die Variable max_eval mit dem Wert negativer Unendlichkeit initialisiert.
  Dies wird in der Regel getan, um sicherzustellen, dass der Anfangswert von max_eval niedriger ist als jede andere Zahl, die im Spiel vorkommen könnte.

* Der Zweck dieser Initialisierung ist, dass max_eval später während des Minimax-Algorithmus aktualisiert wird und den maximalen Wert der Evaluierung für die möglichen Züge des Computers auf dem Spielbrett darstellt.
  Durch die Verwendung von negativer Unendlichkeit als Startwert wird sichergestellt, dass der Wert von max_eval während der Bewertung der Züge des Computers aktualisiert wird, wenn ein besserer Zug gefunden wird.

* In diesem Sinne wird max_eval im Verlauf des Algorithmus schrittweise aktualisiert und enthält schließlich den Wert der maximalen Bewertung für die verfügbaren Züge des Computers auf dem aktuellen Spielbrett.


# eval = minimax(board, depth + 1, False)
* minimax(board, depth + 1, False): Diese Zeile ruft die minimax-Funktion rekursiv auf, um den Wert des aktuellen Spielzustands zu bewerten.
  Die Parameter sind das aktuelle Spielbrett board, die Tiefe des rekursiven Aufrufs erhöht um 1 (depth + 1), und False, um anzuzeigen, dass der nächste Spieler der menschliche Spieler ist (also nicht der maximierende Spieler).

* Durch den rekursiven Aufruf wird der Minimax-Algorithmus fortgesetzt, um den Wert des Spielzustands weiter zu bewerten.
  Wenn die maximale Tiefe erreicht ist oder das Spiel vorbei ist, werden die Endbewertungen des Spielzustands zurückgegeben.
  Andernfalls wird der Algorithmus fortgesetzt, um die besten Züge für den nächsten Spieler zu berechnen.

* Da der nächste Spieler der menschliche Spieler ist (angezeigt durch False), wird die minimax-Funktion weiterhin in einem Modus ausgeführt, der versucht, den bestmöglichen Zug für den menschlichen Spieler zu finden.
  Dies bedeutet, dass die Funktion versucht, den minimalen Wert des Spielzustands zu finden, basierend auf den Zügen des menschlichen Spielers.

* Der Rückgabewert der minimax-Funktion in dieser Zeile ist der Wert des Spielzustands aus Sicht des menschlichen Spielers.
  Dieser Wert wird dann in der Hauptfunktion verwendet, um den besten Zug für den Computer zu finden, basierend auf der Bewertung der möglichen Züge des menschlichen Spielers.