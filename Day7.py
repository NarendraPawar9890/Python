# Match  Case in Python Condition statements

#used to handle multiple cases at the same time 
#handle multiple operations at a same time 

#syntax

# match choice:
    # case1:
    # case2:
    # case3:
    # case_:


# day=int(input("Enter A Day..."))
# print(type(day))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case _:
#         print("Invalid Day No....")


##################################################################

# NO1=int(input("Enter First No.. "))
# NO2=int(input("Enter Second No.. "))

# print(f"""Choose Operation 
#       1.Addition 
#       2.Subtraction 
#       3.Multiplication 
#       4.Division 
#       """
#       )
# Operation=int(input("Enter your choice.. "))

# match Operation:
#     case 1:
#         print("Addition Is :",NO1+NO2)
#     case 2:
#         print(f"Subtraction Is {NO1} - {NO2} = {NO1-NO2}")
#     case 3:
#         print(f"Multiplication IS {NO1} * {NO2} = {NO1*NO2}")
#     case 4:
#         print(f"DIvision IS {NO1} {NO2} = {NO1/NO2}")
#     # case 5:
#     #     print(f"Modulese IS {NO1} % {No2} = {NO1%NO2}")
#     # case 6:
#     #     print(""
#     case _:
#         print("Invalid Choice")


#######################################################################
# Day=input("Enter Day... ")

# match Day:
#     case "Mon"|"Tue" | "Wed" | "Thu" |"Fri":
#         print("Its A Weekday")
#     case "Sat"|"Sun":
#         print("Its A Weekend")
#     case _:
#         print("Invalid Day")
    


##############################################################################################
# Looping Statements In Python

# Execute safe code , multple time 
# Iterting/looping

#for in
# while

#while-
#syntax
#varible init

#while condition :
    # block of code
    # Increment

##################################################################

# a=1
# while a<=10:
#     print("Hello Welcome To Modern Python..",a)
#     a+=1

# b=1
# while b<=100:
#     print(b)
#     b+=1

#Even No
# c=2
# while c<=100:
#     print(c) #2
#     c+=2

# d=1
# while d<=100:
#     if d%2==0:
#         print(d)
#     d+=1

###################################

#Sum of 1 to 50 Even Number

# e=1
# sum=0
# while e<=50:
#     if e%2==0:
#         print(e)
#         sum+=e
#     e+=1
# print("Total Sum is ",sum)


#####################################################################
# for in loop in Python

# for in
# range(start,stop,strp)
# renge(1,10,2)

# for i in range (1,50):
#     print(i)

# for i in range (1,50,2):
#     print(i)

# list=["Narendra","Pratik","Omkar","Bhushan","Arshad"]

# for x in list:
#     print(x)

# sum=0
# for x in range(2,50,2):
#     print(x)
#     sum+=x
# print(sum)


##########################################################################
# break & continue

#break
# Stop Execution Of Program

# for i in range (2,40):
#     if i ==4:
#         break
#     print(i) #2,3


###########continue
# Skip the no

# for i in range (1,10):
#     if i ==4:
#         continue
#     print(i) #1,2,3,5


###################################
# nested for loop

# for i in range (1,5):
#     print (i,"\n")
#     for j in range (1,10):
#         print(j)

#table print
# no=5
# for x in range (1,11):
#     print(no*x)

no=int(input("Enter No..."))
for x in range (1,11):
    print(no*x)