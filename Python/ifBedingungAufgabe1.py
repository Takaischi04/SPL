from random import randint

# Erstelle eine Zufallszahl zwischen 0 und 100
value = randint(0, 100)
		
# Gib die Zufallszahl aus
print("random Int between 0 and 100: ", value)

# Wenn die Zahl kleiner ist als 20  gib aus "Mini"
# Wenn die Zahl zw. 20 und 50 ist gib aus "Medium"
# Wenn die Zahl größer als 50 ist gib aus "Large"
if value < 20:
    print("Mini")
elif value >= 20 and value <= 50:
    print ("Medium")
else:
    print ("Large")

