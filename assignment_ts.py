def begruessung (name): #fehlende Klammer
    print("Hallo,"  + name) # name gross geschrieben
begruessung("Max") # fehlender Aufruf der Funktion

def addiere_zahlen(a, b): # fehlender :
    ergebnis = a + b # fehlender wert
    return ergebnis # fehlender Buchstabe n


def subtrahiere_zahlen(a, b):
    
    return a -b  # falsche Variable


def main(): # fehlender :
    zahl1 = int(input("Gib eine Zahl ein: "))  #fehlende Umwandlung in eine Zahl
    zahl2 = int(input("Gib eine weitere Zahl ein: "))  #fehlende Umwandlung in eine Zahl

    summe = addiere_zahlen(zahl1, zahl2)  
    print("Die Summe ist: ", summe)  # Zahl und string können nicht mit + verknüpft werden

    differenz = subtrahiere_zahlen(zahl1, zahl2)  
    print("Die Differenz ist: ", differenz)  # Zahl und string können nicht mit + verknüpft werden

      

if __name__ == "__main__": # = ist eine Zuweisung.  Vergleich benötigt ==
    main()
   