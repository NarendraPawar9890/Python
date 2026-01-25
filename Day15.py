# # Exception Handeling

# def Calci(a,b):
#     return a/b

# print(Calci(5,5))


# # res=Calci(50,0)
# # print(res)



# ############################
# def Demo(a,b):
#     # print(a+"ABC")
#     print("hello")

# Demo(100,200)

# # next
# def User():
#     print("hello user")
# User()


# print("Hello Welcome....dear")


################################


# Exception handling helps you:

#  Prevent program crashes
#  Handle wrong user input
#  Continue execution even after an error
#  Make programs more professional

try:
    a=20
    b="abc"
    print(a+b)
except:
    print("Error Occured .. ")

print("Hello abc")

##############################
try:
    def Calci(a,b):
        return a/b

    print(Calci(5,5))

    res=Calci(50,0)
    print(res)

except Exception as err:
    print("Error Occured .. ", err)

print("hello")


try:
    age=int(input("Enter Your Age..."))

    def demo(a):
        if a<=0:
            raise ValueError("Age cannot be negative")
        
        print("Your Age is",a)
    demo(age)

except Exception as e:
    print("Error Occured",e)


try:
    a=100
    # b="200"
    # b=int("abc")
    print(a+b)
except ValueError:
    print("Invalid data type ")
except ZeroDivisionError:
    print("Invalid data type")
except TypeError:
    print("wrong data type")

########################################################
#####################################################################


try:
    UserName=input("Enter UserName: ")
    def check(user):
        if not user:
            raise ValueError("UserName cannot be empty")
        if len(user)<4:
            raise ValueError("length must atleast be of 4 length")
        if " " in user:
            raise ValueError("Username must not contain spaces")

        print("Username is valid:", user)
    
    
    check(UserName)
    
except Exception as e:
    print("Error:", e)


# 🎯 1️⃣2️⃣ Practice Tasks
# 1️⃣ Handle division by zero.
try:
    a=1
    b=0
    c=a/b
except Exception as err:
    print("Error Occured .. ", err)

# 2️⃣ Ask for age and handle invalid input.

try:
    age=int(input("Enter Your Age..."))

    def demo(a):
        if a<=0:
            raise ValueError("Age cannot be negative")
        
        print("Your Age is",a)
    demo(age)

except Exception as e:
    print("Error Occured",e)

# 5️⃣ Validate password length (raise error if < 6).
try:
    Password=input("Enter Password:")
    if len(Password)<6 :
        raise ValueError("length cannot be <6")
    print(Password)
except Exception as e:
    print(e)

# # 6️⃣ Create a function that only accepts positive numbers.
# try:
#     no1=int(input("Enter A No:"))
#     if no1 <0:
#         raise ValueError("Enter positive No.")
# except Exception as ee:
#     print(ee)

