from random import randint

# Erstelle ein Würfelspiel! Du spielst gegen den Computer. 
# Wenn das Spiel startet (mit einem kleinen Menü), hat der Spieler 6 Würfe. 
# Er spielt dabei gegen den Computer. Wenn die Augensumme höher ist als jene des 
# Computers hat der Spieler gewonnen, ansonsten der Computer. 
print("- - - - - - -")
print("Würfelspiel")
print("- - - - - - -")

print("1. Cube -> 1 - 6")
print("2. Dodecahedron -> 1 - 12")
print("3. Octagonal bipyramid -> 1 - 16")
print ("-")
starting = int(input("Wähle die Würfelart:"))

# Computer
resultComputer = 0
if starting == 1:
    for diceVar in range(0, 6):
        computerNormalDice = randint(1,6)
        print("Rolls of computer: ", computerNormalDice)
        resultComputer += computerNormalDice
    print("-")
    print("result of computer: ", resultComputer)
    print("-")

elif starting == 2:
    for diceVar in range(0, 6):
        computerDidecahedronDice = randint(1, 12)
        print("Rolls of Computer: ", computerDidecahedronDice)
        resultComputer += computerDidecahedronDice
    print("-")
    print("result of computer: ", resultComputer)
    print("-")

elif starting == 3:
    for diceVar in range(0, 6):
        computerOctagonalDice = randint(1, 16)
        print("Rolls of computer", computerOctagonalDice)
        resultComputer += computerOctagonalDice
    print("-")
    print("result of computer: ", resultComputer)
    print("-")

#Player
resultPlayer = 0
if starting == 1:
    for diceVar in range(0, 6):
        playerNormalDice = randint(1,6)
        print("Rolls of player: ", playerNormalDice)
        resultPlayer += playerNormalDice
    print("-")
    print("result of player: ", resultPlayer)
    print("-")

elif starting == 2:
    for diceVar in range(0, 6):
        playerDidecahedronDice = randint(1, 12)
        print("Rolls of player: ", playerDidecahedronDice)
        resultPlayer += playerDidecahedronDice
    print("-")
    print("result of player: ", resultPlayer)
    print("-")

elif starting == 3:
    for diceVar in range(0, 6):
        playerOctagonalDice = randint(1, 16)
        print("Rolls of player", playerOctagonalDice)
        resultPlayer += playerOctagonalDice
    print("-")
    print("result of player: ", resultPlayer)
    print("-")

if resultPlayer > resultComputer:
    print("Game result: You win!")
elif resultPlayer < resultComputer:
    print("Game result: You lose!")
elif resultPlayer == resultComputer:
    print("Game result: draw!")