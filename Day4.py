# Type Casting
#convert one data type into another data type

age="20"
print(age)
age=int(age)
print(type(age))


# functions ->

# str()
# float()
# bool()

a=20
b="30"
print(a+int(b))

# empId=1234
# print(float(empId))
# print(type(empId))

##################################################
# string concatination

#three type to concatinate -->>
#  "+"
# "," 
#  "f"""

# name = "Aditya"
# print("Your Name is:",name)
# print("Your Name is:"+name)
# print(f'Name is {name}')



# difference of + and , in concatenation

# + it does not convert the data type 
# , it convert the data type 

# num1=100
# num2=23
# print(num1 + num2)

num1="100" # + need same data type to output
num2=23
print(num1 + num2)


################################################
# automatically convert into string
# , - most useful for merg or concat

empRole="Python Developer"
empAddress="Pune"
print(empRole , empAddress )


# f'' -->> clean and modern
empAge = 20
empCTC = "20 LPA"
print(f'Your age is {empAge} and salary is {empCTC}')


age = 20
name = "Priya"
skill = "Python"
print(f'Your name is {name}, Age is {age}, and Skill is {skill}')
# print("Your name is " + name + " Age is " + age + " and Skill is " + skill)
print("Your name is " , name,", Age is ",age,", and Skill is ", skill)

#############################################################################################3333#######################
#  user input

# input() -default data is string

# name= input()
# print("Your Nmae is :" + name)

a = input("Enter the number 1") # Takes the input as string
b = input("Enter the number 2")
print("Addition is ", a+b)

a = int(input("Enter the number 1")) # Takes the input as Integer
b = int(input("Enter the number 2"))
print("Addition is ", a+b)

#######################################################################################################################

#  Reserved Keywords 

import keyword
print("keywords are : ", keyword.kwlist)

########################################################################################################################


# memory Concept
# id - to check memory location of variable
# if value is same then pointed at same memory location
# if value changes of both variables have different memory location
x = 10
print(x)
y = 20
print(y)
print("id of x is",id(x))
print("id of y is",id(y))
################################