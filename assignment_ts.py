def begruessung (name): #fehlende Klammer
    print("Hallo,"  + name) # name gross geschrieben

def addiere_zahlen(a, b): # fehlender :
    ergebnis = a + b
    return ergebnis # fehlender Buchstabe n

def subtrahiere_zahlen(a, b):
    return a - b # falsche Variable

def main(): # fehlender :
    zahl1 = input("Gib eine Zahl ein: ")  
    zahl2 = input("Gib eine weitere Zahl ein: ")  

    summe = addiere_zahlen(zahl1, zahl2)  
    print("Die Summe ist: " + summe)  

    differenz = subtrahiere_zahlen(zahl1, zahl2)  
    print("Die Differenz ist: " + differenz)  

    begruessung("Max")  

if __name__ == "__main__": # = ist eine Zuweisung.  Vergleich benötigt ==
    main()