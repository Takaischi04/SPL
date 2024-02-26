print("1. Einzahlen")
print("2. Abheben")
print("3. Kontostand")
print("4. Beenden")
userInput = input("Was möchten sie machen: ")

balance = 0;

def AddToBalance(balance, amountToAdd):
    balance = balance + amountToAdd
    print(amountToAdd," wurde eingezahlt")

if userInput == 1:
    amountToAdd = input("Wieviel soll eingezahlt werden: ")
    AddToBalance(amountToAdd)

elif userInput == 2:
    amountToRemoce = input("Wieviel soll abgehoben werden: ")
