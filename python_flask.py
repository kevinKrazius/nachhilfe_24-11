## Aufgabe: Zahlenraten-Spiel
# 
# Schreibe ein Programm, das ein einfaches Zahlenraten-Spiel implementiert. Hier sind die Anforderungen:
# 1. Das Programm wählt eine zufällige Zahl zwischen 1 und 10.
# 2. Der Benutzer gibt eine Zahl ein, um die richtige Zahl zu erraten.
# 3. Das Programm gibt Hinweise, ob die geratene Zahl zu hoch, zu niedrig oder korrekt ist.
# 4. Das Spiel wiederholt sich, bis die richtige Zahl erraten wurde.
# 5. Verwende eine Schleife und Bedingungen, um das Spiel zu steuern.
# 6. Stelle sicher, dass das Programm keine Fehler ausgibt, wenn die Benutzereingabe keine Zahl ist.
#
# Hier ist eine Vorlage mit den einzelnen Schritten:

# 1. Importiere das Modul, das dir hilft, eine zufällige Zahl zu generieren.

import random

# Erkläre dem Benutzer, was das Programm macht.
def zahlenraten():
    print("Willkommen zum Zahlenratenspiel.")
    print("Ich habe eine Zahl zwischen 1 und 100 gewählt. Kannst du sie erraten?")

# Generiere eine zufällige Zahl zwischen 1 und 100.
    richtige_zahl = random.randint(1, 100)
    geraten = False

# Starte eine Schleife, in der der Benutzer immer wieder eine Zahl raten kann.
    while not geraten:
        try:
        # Hole die Eingabe vom Benutzer und stelle sicher, dass sie eine Zahl ist.
            tipp = int(input("Dein Tipp (eine Zahl zwischen 1 und 100): "))
        
        # Vergleiche die Benutzereingabe mit der zufälligen Zahl:
            if tipp < richtige_zahl:
                print("Zu niedrig. Versuche es nochmal.")
            elif tipp > richtige_zahl:
                print("Zu hoch. Versuche es nochmal.")
            else:
                print(f"Richtig. Die Zahl war {richtige_zahl}. Glückwunsch.")
                geraten = True
        except ValueError:
            print("Bitte gib eine gültige Zahl ein: ")


zahlenraten()
