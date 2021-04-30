#Definition
def Leibnizreihe(Anzahl):

#Variablen 0 setzen
    k, ergebnis = 0, 0
    
#while Schleife mit Bedingung und Formel
    while k < Anzahl:
        ergebnis, k = ergebnis+((-1)**k)/(2*k+1), k +1 
    return 4*ergebnis

#Ausgabe     
print(Leibnizreihe(int(input('Anzahl iteration:\n'))))
