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
            # Wenn die Eingabe keine Zahl ist, gib eine Fehlermeldung aus und lass den Benutzer erneut raten.
            print("Bitte gib eine gültige Zahl ein: ")

# Rufe die Funktion auf, um das Spiel zu starten.
zahlenraten()
