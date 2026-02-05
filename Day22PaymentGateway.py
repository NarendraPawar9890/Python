# Flow
# 1.insert 
# 2.enter pin
# 3.choose opr
# 4.perform opr
# 5.handle error

#Step 1 : Create Bank Account Class
# balance , pin 

class BankAccount:
    def __init__(self,pin,balance=0):
        #create instance variables and stored in obj
        self.balance=balance
        self.pin=pin

        #method to verify pin

    def verifyPin(self,user_pin):
        if user_pin!=self.pin:
            raise ValueError("Invalid Pin...")
        return True 
            
    def reset_pin(self,old_pin,new_pin):
        self.verifyPin(old_pin)
        self.pin=new_pin
        print("Pin reset Done...")


class ATM:
    def __init__(self,account):
        self.account=account
    def Withdrawal(self, amount):
        if amount<=0:
            raise ValueError("Invalid Amount...")
        if amount > self.account.balance:
            raise ValueError("Insufficient Amount...")
        self.account.balance-=amount
        print ("Money Withdrawal Successfully...")
        print ("Current Balance is : ",self.account.balance)

    def Deposit (self, amount):
        if amount <= 0:
            raise ValueError ("Invalid Amount....")

        self.account.balance +=amount

        print("Money Deposite successfully")
        print ("Current Balance is :",self.account.balance)

    def CheckBalance(self):
        print ("Balance is :",self.account.balance)
    

#step 2 - User Interface
account=BankAccount("7219",1000000)
atm=ATM(account)

try:
    your_pin=input('Enter Your Pin..')
    account.verifyPin(your_pin)
    while True:
    
        print("\n ATM MENU...")
        print("1.Withdraw..")
        print("2.Deposit.")
        print("3.Check Balance.")
        print("4.Reset Pin.")
        print("5.Exit")

        choice=input("Enter Your Choice : ")

        match choice:
            case "1":
                amount=int(input("Enter Withdrawal Amount : "))
                atm.Withdrawal(amount)

            case "2":
                amount=int(input("Enter Deposite Amount : "))
                atm.Deposit(amount)

            case "3":
                atm.CheckBalance()         

            case "4":
                oldpin=input("Enter Old Pin : ")
                account.verifyPin(oldpin)
                newPin=input("Enter New Pin : ")
                account.reset_pin(oldpin ,newPin)

            case "5":
                print("Thanks...")
                break

            case _:
                print("Invalid Choice..")

except Exception as e:
    print ("Error Occured...",e)