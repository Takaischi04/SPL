balance = 0

while True:
    print("1. Einzahlen")
    print("2. Abheben")
    print("3. Kontostand")
    print("4. Beenden")
    userInput = int(input("Was möchten sie machen: "))

    def AddToBalance(amountToAdd):
        global balance
        balance = balance + amountToAdd
        print("-")
        print(amountToAdd," wurde eingezahlt")
        print("-")

    def removeFromBalance(amountToRemove):
        global balance
        balance = balance - amountToRemove
        print("-")
        print(amountToRemove," wurde abgehoben")            
        print("-")

    if userInput == 1:
        amountToAdd = int(input("Wieviel soll eingezahlt werden: "))
        AddToBalance(amountToAdd)

    elif userInput == 2:
        amountToRemove = int(input("Wieviel soll abgehoben werden: "))
        removeFromBalance(amountToRemove)

    elif userInput == 3:
        print("-")
        print("Kontostand: ", balance)
        print("-")

    elif userInput == 4:
        print("-")
        print("shutting down")
        print("-")
        break