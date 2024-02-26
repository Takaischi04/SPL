from random import randint
# Erstelle eine Funktion die 2 Zahlen addiert
print("Function 1")

def Function1(number1, number2):
    result = 0
    result = number1 + number2
    print(result)

Function1(5,6)

print("-----")
# Erstelle eine Funktion, die eine zufällige Zahl zwischen 100 und 200 zurückliefert
print("Function 2")

def Function2(randomValue):
    print(randomValue)

Function2(randint(100,200))

print("-----")
# Erstelle eine Funktion, die ein Wort aus einem String Array zurückliefert. 
#     z.B. ["hans", "peter", "susi"] 
#     Die Funktion liefert zufällig eines der Worte zurück
print ("Function 3")

def Function3(randomName):
    name = ["Hans", "Peter", "Susi"]
    print("generated Value: ", randomName)
    if randomName == 1:
        print(name[0])
    elif randomName == 2:
        print(name[1])
    else:
        print(name[2])
Function3(randint(1,3))