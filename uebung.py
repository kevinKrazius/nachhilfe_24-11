import random

# Erkläre dem Benutzer, was das Programm macht.
def zahlenraten(): # Hier wird die Funktion Zahlenraten() definiert, die das Spiel enthält. Sie hat keine Parameter und führt das gesamte Spiel durch.
    print("Willkommen zum Zahlenratenspiel.") # Diese beiden Printbefehle geben eine Begrüßung und eine kurze Erklärung aus.
    print("Ich habe eine Zahl zwischen 1 und 100 gewählt. Kannst du sie erraten?") # 
    
    # Generiere eine zufällige Zahl zwischen 1 und 100.
    richtige_zahl = random.randint(1, 100) # Durch die Funktion random.randit wird eine zufällige Zahl zwischen 1 und 100 generiert. Diese wird in richtige_zahl gespeichert.
    geraten = False # Die Variable geraten wird auf False gesetzt und dient dazu, die while-schleife zu kontrollieren-solange sie nicht erranten wird, bleibt sie False.

    # Starte eine Schleife, in der der Benutzer immer wieder eine Zahl raten kann.
    while not geraten: # Die while-Schleife läuft, solange geraten == False ist. Sobald die richtige Zahl geraten wird, wird geraten == True und die Schleife stoppt.
        try:
            # Hole die Eingabe vom Benutzer und stelle sicher, dass sie eine Zahl ist.
            tipp = int(input("Dein Tipp (eine Zahl zwischen 1 und 100): ")) # Der Code fordert den Benutzer auf, eine Zahl einzugeben. input() gibt standardmäßig einen String zurück, 
            # daher wird mit int() eine Umwandlung in eine ganze Zahl (int) durchgeführt.

            # Vergleiche die Benutzereingabe mit der zufälligen Zahl:
            if tipp < richtige_zahl:
                print("Zu niedrig. Versuche es nochmal.") # Falls die geratene Zahl (tipp) kleiner als die richtige Zahl (richtige_zahl) ist, wird "zu niedrig" ausgegeben.
            elif tipp > richtige_zahl:
                print("Zu hoch. Versuche es nochmal.") # Falls die geratene Zahl größer ist, wird "zu hoch" ausgegeben.
            else:
                print(f"Richtig. Die Zahl war {richtige_zahl}. Glückwunsch.") # Falls "tipp" die richtige Zahl ist, wird eine Glückwunschmeldung ausgegeben und 
                geraten = True      # geraten wird auf True gesetzt und die Schleife beendet.
        except ValueError:
            # Wenn die Eingabe keine Zahl ist, gib eine Fehlermeldung aus und lass den Benutzer erneut raten.
            print("Bitte gib eine gültige Zahl ein: ")

# Rufe die Funktion auf, um das Spiel zu starten.
zahlenraten()
