from random import randint

# Erstelle zwei Zufallszahl zwischen 0 und 100
value1 = randint(0, 100)
value2 = randint(0, 100)

print("Zahl 1: ", value1)
print("Zahl 2: ", value2)

# Wenn die erste Zahl kleiner ist als die zweite UND die erste Zahl kleiner ist als 50
# dann gib aus "Zahl 1 ist kleiner als Zahl 2 und Mini"
if value1 < value2 and value1 < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")
		
# Wenn die erste Zahl kleiner ist als 30 oder die zweite Zahl kleiner ist als 30
# dann gib aus "Eine der beiden ist kleiner als 30"
elif value1 < 30 or value2 < 30:
    print("Eine der beiden ist kleiner als 30")
		
# Wenn die erste Zahl kleiner ist als 50 UND die zweite Zahl ungleich 50 ist
# dann gib aus "Erste Zahl klein, zweite kein 50iger"
elif value1 < 50 and value2 != 50:
    print("Erste Zahl klein, zweite kein 50iger")

else:
    print("keine Angabe")