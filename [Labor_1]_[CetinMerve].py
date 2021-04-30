#Aufgabe 1:
# Schreiben Sie ein Phyton-Programm,das
# 1) den Benutzer begrüßt
# 2) eine erste Zahl etngegen nimmt
# 3) eine zweite Zahl entgegen nimmt 
# 4) die Summe der beiden Zahlen berechnet und ausgibt
# 5) die Differenz der beiden Zahlen berechnet und ausgibt
# 6)das Produkt der beiden Zahlen berechnet und ausgibt
# 7)den Quotient der beiden Zahlen berechnet und ausgibtn(ink.Nachkommastellen)


# Benutzer Begrüßen
print("Hallo BenutzerIn")

Zahl1_string = input ("Eingabe der ersten Zahl:")
Zahl1 = int(Zahl1_string)
Zahl2_string = input ("Eingabe der zweiten Zahl:")
Zahl2 =int(Zahl2_string)


#Berechnung der Summe
summe= Zahl1 + Zahl2
print(summe)

#Berechnung Differenz
Differenz = Zahl1 - Zahl2
print(Differenz)

#Berechnung Produkt
Produkt = Zahl1*Zahl2
print(Produkt)

#Berechnung Quotient
Quotient = Zahl1 / Zahl2
print(Quotient)
