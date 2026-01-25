# Default Parameter

# def Sum(a,b):
#     print(a+b)

# Sum(20,50)
# Sum(20)

# Default Parameter- such a  default values which we pass during function declartion 
# used when user doesnt passed sufficient arguments

# default parameters -

def sum(a=0,b=0):
    print(a+b)

sum(2,4)
sum(3)
sum()

###########################
def Mult(a=1,b=1):
    print(a*b)

Mult(5,4)
Mult()
Mult(4)

#####################################

def Emp(empName="JOHN",empSkill="React",empId=None):
    return empName, " And ", empSkill, " And ", empId

# print(Emp())
# print("","Python")
# print (Emp("","JS") )|

print(Emp(empSkill="Devops",empName="Pratik",empId=123))


###########################################################################33

# Arguments -
# used to handle extra arguments which we passed during function calling 
# *args

def add (a=0,b=0,*args):
    print(args)
    sum=a+b
    for x in args:
        print(x)
        sum+=x
    
    print("Total Sum is :",sum)

add(3,4,2,5,6,6)
add()

#####################################################

# Recurrsive function

# def Demo(parameter):
#    if base_condition:
#       return some_value
#    else:
#       return Demo(some_value)