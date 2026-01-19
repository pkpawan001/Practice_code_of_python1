class Card:
    def __init__(self):
       self.cardnumber=input("Enter your 16 digit card number")
    
    def showNumber(self):
        self.lastDigit=self.cardnumber[15:]
        self.hide=4*'X'+" "
        print("Your card number is:")
        print(4*self.hide + self.lastDigit)

    
c1=Card()
c1.showNumber()

