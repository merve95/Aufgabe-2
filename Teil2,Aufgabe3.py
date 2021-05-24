woerterbuch_deutsch = ["Katze", "Hund","Hase","Schildkröte","Löwe","Vogel"]
print(len(woerterbuch_deutsch))
woerterbuch_english = ["cat", "dog","rabbit","turtle","lion","bird"]
max = len(woerterbuch_deutsch)

eingabe = input ("Deutscher Begriff:")

eingabe = input ("Englischer Begriff:")


index = 0

while index < max :
    
    if woerterbuch_deutsch[index] == eingabe:
        print(woerterbuch_english[index])
        break
    index +=1
if index == max:
    print("nicht gefunden")
f:")

woerterbuch_english = ["cat", "dog","rabbit","turtle","lion","bird"]
print(len(woerterbuch_english))
woerterbuch_deutsch = ["Katze", "Hund","Hase","Schildkröte","Löwe","Vogel"]
max = len(woerterbuch_english)


index = 0

while index < max :
    
    if woerterbuch_english[index] == eingabe:
        print(woerterbuch_deutsch[index])
        break
    index +=1
if index == max:
    print("nicht gefunden")
    
index = 0




