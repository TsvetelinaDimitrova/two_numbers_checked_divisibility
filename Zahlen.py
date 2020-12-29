#Zahlen
zahl1 = float (input ("Eingabe Zahl1: "))
zahl2 = float (input ("Eingabe Zahl2: "))
if zahl1>=zahl2:
    if zahl1%zahl2 == 0:
        if zahl1==zahl2:
            print("Zahlen sind gleich")
        else:
            print("Zahlen sind teilbar")
    else:
        print("Zahlen sind nicht teilbar")
else:
    print("Zweite Zahl ist größer als erste Zahl")
input("Beenden mit Eingabetaste")