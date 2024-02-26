# Erstelle ein Programm, dass Zufallszahlen zwischen 10 und 30 generiert.
# Das Programm soll die Zufallszahlen zusammenzählen.
# Sobald die Zahl 15 oder die Zahl 25 kommt, wird das Programm beendet und die Summe der vorherigen Zufallszahlen ausgegeben!

from random import randint

startValue = randint(10, 30)
result = 0

print("Starting: ", startValue)

while True:
        valueToAdd = randint(10, 30)
        print("Value to add: ", valueToAdd)
        result += valueToAdd
        
        if valueToAdd == 15 or valueToAdd == 25:
            break
        
print("End Result: ", result)