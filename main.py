#function to collect input i.e amount from user and validate if it is correct
def deposit():
    while True:
        amount= input("what would you like to deposit?$")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("amount should be greater than 0")
        else:
            print("Please enter a number")

    return amount

deposit()
