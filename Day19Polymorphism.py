# Polymorphism- one method have difffernt / multiple behavior based on arguments, operators, object, class 


# Run Time Polymorphsim ( Method Overiding ) / Polymorphism with Inheritance (Method Overriding)

class Parent:
    def hello(self):
        print("hello parent class")

class Child(Parent):
    def hello(self):
        print("hello child class")
        # super().hello()


child1=Child()
child1.hello()

###################################################

class Payment:

    def __init__(self,wallet_balance,order_id,status,customer_id):
        self.wallet_balance=wallet_balance
        self.order_id=order_id
        self.status=status
        self.customer_id=customer_id


    def details(self):
        print("Hello Details Method in Parent class.....")
        print(f"""Wallet Balance : {self.wallet_balance} , order Id {self.order_id} , 
               status = {self.status} and customer Id. {self.customer_id} """)


class UPI(Payment):

    def details(self):
        print("Hello UPI Details.......")
        super().details()

    def pay(self):
        print("Pay Here ........")
    

class COD(Payment):
    def pay(self):
        print("Pay - COD")

    
payment=UPI("100000","#123","Order Placed","1234567")
payment.details()

UPI1=UPI("7997847","#763","Order Cancle","8727638")
UPI1.pay()
UPI1.details()

COD1=COD("uhegdf","#098","Order Successfull","45678")
COD1.pay()
COD1.details()
print(COD1.customer_id)

#################################################################################################################

# method Overloading - compile time polymorphism
# python does not support true overloading
# but we can achive using args


class Calculator:
    def sum(self,a,b,c,*args):

        for x in args:
            print(a+b+c+x)
        # print(a+b+c)

result1=Calculator()
result1.sum(10,20,30)
result1.sum(10,20,30,100,200,300)


# Operator overloading
# same operator but differenet behavior

# len(), +
# type()

string="Pratik"
list=["A","b","C"]
tuple_1=(10,20,30,50)
print(len(string))
print(len(list))
print(len(tuple_1))

# +

print(10+20)
print("ABC"+"PQR")

print(str(10)+"20")
a=str(10)
print(a)