# Functions in python-
# Function is block of code 
# Can

'''
Syntax-

def function_name():
    //Block of code
#function_call
function_name()

eg

def demo():
    print("hello world)

demo()
'''



# print("Welcome to Python Functions")

# def demo():
#     print("Hello Function")

# demo()
# demo()

# def Add():
#     print(30+20)
# Add()
# Add()

# # To make the the function dynamic 
# # Parameters - valuse passed during fun_declaration
# # Arguments-Actual values passed during function calling

# def Sum(a,b):
#     print(a+b)
# Sum(10,20)
# Sum(30,50)

# #################################################
# def CheckEligibility(age):
#     if age>=18:
#         print("You are Eligible")
#     else :
#         print("Sorry.. You are nat eligible")

# userage=int(input("Enter Your Age"))
# CheckEligibility(userage)
# # CheckEligibility(20)




# ####################################################################################################
# # return- Used to return values outside the functions itself
# # Its stops the executing of our program after returning

# def EvenOdd(no):
#     result="Even No" if no%2==0 else "Odd NO"
#     return result

# print(EvenOdd(30))
# print(EvenOdd(37))

# def demo(name, skill):
#     print (name+" "+skill)
#     return name+skill
#     print("hello world")

# demo("abc","py")


# def UserInfo(userName,userSkill,userAddress):
#     print(f"Your Name is {userName}, Your Skill is {userSkill} and your Address is {userAddress}")

# UserInfo("Narendra","Python","Anagar")
# UserInfo("ABC","JS","Mumbai")


# def deposit (balance):
#     added = int(input("Enter amount to be deposit :"))
#     balance+=added
#     print(balance)
    

# def withdraw (balance):
#     withdrawal = int(input("Enter amount to be withdraw :"))
#     balance-=withdrawal
#     print(balance)
  
# def main ():
#     account_balance= 100000
#     action = input("Enter deposit or withdraw :").lower()
#     match action :
#         case "deposit":
#             account_balance = deposit(account_balance)
#         case "withdraw":
#             account_balance = withdraw(account_balance)
#         case "no":
#             print("Account Balance:", account_balance)
#         case _:
#             print("Invalid choice")
         

        
# main()


############################################################################################3
# Task Python E-Wallet System
wallet_balance = 50000

def add (balance):
    Value_toadd =int(input("Enter Amount to add :"))
    if Value_toadd <= 0:
        print(" Amount must be positive.")
    else:
        balance+= Value_toadd
        print(" Money added successfully.")
        print("Balane is:",balance)
    return balance

def withdraw(balance):
    Value_toWithdraw = int(input("Enter amount to Withdraw :"))
    if Value_toWithdraw<=0:
        print("Amount must be positive.")
    elif Value_toWithdraw>balance:
        print("Insufficient balance.")
    else:
        balance-= Value_toWithdraw
        print("Money withdrawl successfully")
        print("Balane is:",balance)
    return balance

def checkBalance(balance):
    print("Balane is:",balance)
    return balance

while True :
    print("****Menu****")
    print("1. Add Amount")
    print("2. Withdraw Amt")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter Choice :").lower()
    if choice == '1' or choice =='add':
        wallet_balance = add(wallet_balance)

    elif choice =='2' or choice == 'withdraw':
        wallet_balance = withdraw(wallet_balance)
    elif choice == '3' or choice == 'checkbalance':
        wallet_balance =checkBalance(wallet_balance)
    elif choice == '4' or choice == 'exit':
        break
    else :
        print("Invalid input")
        