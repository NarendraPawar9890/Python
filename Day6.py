# Condition statements in Python


#################################################################################
# If statement----

# shop_amount=int(input("Enter Shopping Amount"))
# if(shop_amount>=20000):
#     disc_amount=shop_amount*30.2

# print("Your Final Amount=",shop_amount-disc_amount)

##############################################################################
# if else Statements-----

# no=int(input("Enter a number:"))
# if(no%2==0):
#     print("Even No")
# else:
#     print("Odd No")

################################################################################

# if else if 

Shop_Amo=int(input("Enter shopping amount :"))

if(Shop_Amo>=10000 and Shop_Amo<=20000):
    disc=20
    # disc=Shop_Amo*disc/100
elif(Shop_Amo>=20000 and Shop_Amo<=30000):
    disc=30
    # disc=Shop_Amo*disc/100
elif(Shop_Amo>=30000 and Shop_Amo<=40000):
    disc=40
    # disc=Shop_Amo*disc/100
elif(Shop_Amo>=40000):
    disc=50
    # disc=Shop_Amo*disc/100
else:
    print("No Discount")

#membership operators
#in
#not in

#print("membership Operators In Python")

data=[20,40,60,100,30,"OM","Aditya","Sanmesh",True,None,23.5]

# Membership Operator

# in and not in= check whether element is present or not
print("OM" in data) # True
print("ABC" not in data) # True


# Identity Opertor
# is and is not- check whether same object memory or not

a=10
b=a
c=[10,20,30]
print(a is b)
print(a is c) # False
print(a is not b) # False

####################################################################


# Control Statement- controlling the statements- Decision making power

# Conditional Statements- check conditions( True / False ) and return output 



# ternary operator-   "output If True" if condition else "output is false"

# if 
# if else
# if elif else
#  match–case (Python 3.10+ Switch Case) - Switch case


# Looping statements
   # In python- for in and while only

######################################################################################


# if statement- check 1 condition at a time

# if(condition):
    # block of code



# number=int(input("Enter A Number...To Check given no is even or odd"))
# if(number%2==0):
#     print("Even NO = ", number)

# if(number%2!=0):
#     print("Odd No", number)


# ***************************

# eg 2

# age=float(input("Enter Your Age"))
# if(age>=18):
#     print("You Are Elgible For Voting...")


# if(age<18):
#     print("Sorry Bhai....")

# *******************************
# take a shopping amount from user as a input
# and if shop_amt>=20000
# disc=20%
# else disc=0

# Print All the details


shop_amt=int(input("Enter Shopping Amount.."))
disc=0

if(shop_amt>=20000):
    disc=10

if(shop_amt<20000):
    disc=0

disc_amt=shop_amt*disc/100
net_Total=shop_amt-disc_amt


# print(f"Your Shopping Amount Is {shop_amt} \n")
# print(f"You Got A {disc}% \n")
# print(f"Your Discount Amt is {disc_amt}")

# print(f"Net Total Is {net_Total}")



# ***********************************

# if else- used to check 2 conditions at a same time

# if(condition):
#     # block of code
# else:
#     # block of code





# if(True):
#     print("hello ......dear")
# else:
#     print("Bye bye")


age=int(input("Enter Your Age.."))
if(age>=18):
    print("Congrats...")
else:
    print("Sorry")


############################################################################################

no=int(input("Enter A No"))
if(no%2==0):
    print("Even No")
else:
    print("Odd No")


############################################################################################

score1=int(input("Enter SCore 1..."))
score2=int(input("Enter SCore 2..."))
score3=int(input("Enter SCore 3..."))
score4=int(input("Enter SCore 4..."))
score5=int(input("Enter SCore 5.."))
score6=int(input("Enter SCore 6..."))

if(score1>=35 and score2>=35 and score3>=35 and score4>=35 and score5>=35 and score6>=35):
    # print("Pass....")

    per=((score1+score2+score3+score4+score5+score6)/600)*100
    # print(per)

    if(per>=75):
        print("You Got a distinction", per)
    else:
        print("Pass Class")


else:
    print("fail")


############################################################################################

# # if elif else- to check 2 or more conditions at a same time

# if(conditon):
#     # block of code
# elif(condition):
#     # block of code
# elif(condition):
#     # block of code
# else:
#     # block of code


a=int(input("Enter No 1 : "))
b=int(input("Enter No 2 :"))
c=int(input("Enter No 3 : "))

if(a>=b and a>=c):
    print("A is larger No", a)
elif(b>=a and b>=c):
    print("B is Larger No ",b)
else:
    print("C Is Larger No ",c)


####################################################################################################

shop_amt=int(input("Enter A Shopping Amount"))
disc=0
if(shop_amt>=10000 and shop_amt<20000):
    disc=20
elif(shop_amt>=20000 and shop_amt<30000):
    disc=30
elif(shop_amt>=30000 and shop_amt<40000):
    disc=40
elif(shop_amt>=40000):
    disc=50
else:
    print("No Discount")



disc_amt=shop_amt*disc/100
net_Total=shop_amt-disc_amt

print(f"Your Shopping Amount Is {shop_amt} \n")
print(f"You Got A {disc}% \n")
print(f"Your Discount Amt is {disc_amt}")

print(f"Net Total Is {net_Total}")



# Shoping amt
shop_amt=int(input("enter the amount of your shoping"))
if(shop_amt>=10000 and shop_amt<20000):
    print("congrats you have discont of 20%")
elif(shop_amt<=30000 and shop_amt>40000):
    print("you have discont 40%")
elif(shop_amt>=40000 ):
    print("you have discont 50%")
else:
    print("no discont")

disc=Shop_Amo*disc/100
print("Discount Amount =",disc)
print("Net Amount=",Shop_Amo-disc)