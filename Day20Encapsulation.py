# Encapsulation- security
# Hides the Data
# Avoid misused
# There are 3 Access modifiers
# public- free access - name
# private - strictly hidden-   __name
# protected- internal use only-  _name

################################################################\

class Account:
    try:
        def __init__(self):
            self.__balance = 0

        def deposit(self, amount):
            self.__balance += amount

        def withdraw(self, amount):
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient Balance")

        def check_balance(self):
            return self.__balance
        
    except Exception as e:
        print("Error Occured : ",e)


try:
    acc = Account()
    acc.deposit(5000)
    print(acc.check_balance())
    acc.withdraw(2000)
    print(acc.check_balance())

except Exception as e:
        print("Error: ",e)

        
class A:
    # public member
    # class Variable
    acc_no=1234567890

    def AccountHolder(self,userName,userId):
        # instance variable
        print("Hello Dear....")
        self.userName=userName
        self.userId=userId

        # by default function return None
        return f"Your Name Is {self.userName} and user ID is {self.userId}"

        
user1=A()
result1=user1.AccountHolder("Pratik",123)
print(result1)
        


################################################
class A:

    # public member
    name="Narnedra"

    # private  member
    __empCTC="2LPA"

    # protected members
    # access but not modified
    _empRole="Devloper"

    def Details(self):
        
        self.empId=73646
        # print(self.name)
        print(self.empId)

        # private
        print(self.__empCTC)

        # protected
        print(self._empRole)


class B(A):
    skill="Python"
    print(skill)

result1=B()
result1.Details()

# public member
print(result1.name)

# private member
# print(result1.__empCTC)

# can we access private members
# Python uses name mangling internally:

print(result1._A__empCTC)

# protected members
# we can access but its says dont modifed but we can modified ie. its just a convention in python
print(result1._empRole)