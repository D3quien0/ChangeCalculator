
def quarterAmount(changeBack):
    numOfQuarters = 0
    while changeBack >= 25:
        changeBack -= 25
        numOfQuarters += 1
    print(numOfQuarters, ' quarter/quarters')
    dimeAmount(changeBack)

def dimeAmount(balanceRemaining):
    numOfDimes = 0
    while balanceRemaining >= 10:
        balanceRemaining -= 10
        numOfDimes += 1
    print(numOfDimes, ' dime/dimes')
    nickelAmount(balanceRemaining)

def nickelAmount(changeDue):
    numOfNickels = 0
    while changeDue >= 5:
        changeDue -= 5
        numOfNickels += 1
    print(numOfNickels, ' nickel/nickels')
    pennyAmount(changeDue)

def pennyAmount(moneyDebted):
    numOfPennies = 0
    while moneyDebted >= 1:
        moneyDebted -= 1
        numOfPennies += 1
    print(numOfPennies,' penny/pennies')
    while True:
        try:
            repeat = input('Would you like to continue (y)es or (n)o: ')
            if repeat == 'y':
                cambio = float(input("How much change does the customer need: "))
                cambio *= 100
                quarterAmount(cambio)
                break
            elif repeat == 'n':
                break
        except ValueError:
            print('Please try again.')
            continue

            

while True:
    try:
        change = float(input("How much change does the customer need: "))
        change *= 100
        quarterAmount(change)
        break
    except ValueError:
        print('Invalid entry, please try again.')
        continue
    