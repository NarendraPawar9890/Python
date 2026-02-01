# oop in python 
# OOP_ is of professional way of writing our code to solve real world problmens

# like- Avoid Code Reptition
# Securtity and Proetection
# Easy Maintainance
# Oragnaized Code

# OOP 4 Pillars
# Inhertiance
# Polymorphim
# Encapsulation
# Asbtraction

# OOP has class and Objects

# Class- is a real time entity having methods and properties
        # is a blueprint of a object

# eg- class Mobile- class
        #   Properties / attributes/ variables - name,color,brand,ram,rom,
        # methods/ action/ function - calling, switchon,switchoff,chatting
 
 
# object- instance of a class
# eg we can create 1000 of mobile by using same mobile class 


# # creating clas
# class Mobile:
#     pass


# # creating object
# m1=Mobile()
# m2=Mobile()

# *************************

# eg

class Mobile:
    # properties / variables
    name="Iphone 18 pro"
    brand="Apple"
    color="Midnight Black"

    # methods
    def calling(self):
        print("hello i am busy on call.....")
    
    def chatting(self):
        print("i am chatting with someone...")

    def camera(self):
        print("CLicking photos....")


m1=Mobile()
print(m1.name)
print(m1.brand)

m1.calling()
m1.chatting()
m1.camera()
# Bank Account	A specific savings account (e.g., John Doe's account #12345)	Account number, holder name, balance, address	deposit(), withdraw(), checkBalance()


class Bank_Account:
    Account_No=928488748
    Holder_Name="abc"
    Balance=1000


    def deposit(self):
        print("Deposite Amt")
        
    def withdraw(sdelf):
        print("Withdraw Amt") 
        
    def checkBalance(self):
        print("Check Balance")

B1=Bank_Account()
print(B1.Account_No)
print(B1.Holder_Name)
print(B1.Balance)

B1.deposit
B1.withdraw
B1.checkBalance


######################################################################
class Manga:
    Title="One Pice"
    Author="Eiichiro Oda"
    Publisher="Shonen Jump"
    Number_Of_Chapters=1171
    Status="Not Complete"

    def open_chapter(self):
        print("Open a Chapter")

    def colse_chapter(self):
        print("Close a Chapter")

M1=Manga()
print("Title:",M1.Title)
print("Author:",M1.Author)
print("Publisher:",M1.Publisher)
print("Numbers Of Chapters:",M1.Number_Of_Chapters)
print("Status:",M1.Status)

M1.open_chapter()
M1.colse_chapter()