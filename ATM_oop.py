class ATM:
# Main portal where all thing get start
    def __init__(self):
        self.balance=0
        self.pin=""
        self.atmcard()
# First mainu that apper at screean
# first you have to put your pin random and remember it for other things in it 
    def atmcard(self):
        print("")
        self.space()
        print("Please inseart your ATMcard")
        user_pin = input("enter your pin---> ")
        self.pin = user_pin
        self.space()
        self.MainMenu()
    
    def enterPin():
        user_pin= (input("Enter your pin:-"))

    def MainMenu(self):

        user_input = int(input("Press 1 for \n---->Check balance<----\nPress 2 for\n---->Change pin<----\nPress 3 for \n---->withdraw<----\nPress 4 for \n ---->Deposite<----\n ====> "))
        
        if user_input == 1 :
            self.check_balance()
        elif user_input ==  2 :
           self.ChangePass()
        elif user_input == 3 :
            self.withdraw()
        elif user_input == 4 :
            self.deposit()
        elif user_input == 5 :
            exit
        else:
           self.MainMenu()
        
    def space(self):
        print("**********************")

    def check_balance(self):
        self.space()
        user_pin = (input("plz enter your pin--->"))
        if user_pin == self.pin:
            self.space
            print(f"Your balance  is {self.balance}")
            self.space()
            self.MainMenu()
        else:
                print("plz enter corret pin")
                self.space()
                self.MainMenu()

    def ChangePass(self):
        self.space()
        user_pin= (input("Enter your pin:-"))
        if user_pin == self.pin:
            user_newpin = (input("Enter your new pin:-"))
            self.pin = user_newpin
            print("Your pin is now succesfully change")
            self.space()
            self.MainMenu()
        else:
            print("Plz enter the corret pin again")
            self.space()
            self.MainMenu()

    def withdraw(self):
        self.space()
        user_cash = int(input("Enter how much you need to withdraw\n---->"))
        if user_cash<self.balance:
            self.balance=self.balance - user_cash
            print(f"Now you have {self.balance} balance in your account")
            self.space()
            self.MainMenu()
        else:
            print("You do not have that much mommy in your bank")
            self.space()
            self.MainMenu()

    def deposit(self):
        self.space()
        user_balance=int(input("Enter how much you want to deposit\n----->"))
        self.balance=self.balance + user_balance
        print(f"Now you have {self.balance} balance in your account")
        self.space()
        self.MainMenu()


pratyanj = ATM()