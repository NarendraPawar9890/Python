

class Emp:
    # properties/ attributes
    empId=1234,
    empRole="Developer",
    empCTC="20LPA"

    # methods

    # self- this keyword
    # reference variable i.e refer to current objects methods and properties
    def PersonalDetails(self):
        print("Methods")
        

# instance
emp1=Emp()
print(emp1.empId)
print(emp1.empCTC)
print(emp1.empRole)

emp1.PersonalDetails()

####################################################################

# without constructor

class Company:

    # class variable-accessible thorugh out class
    company_name="Infosis"

#  Why `self` is required?
#  To store data **inside the object**
#  To give **each object its own separate variables**
#  To access object variables **inside methods**

    def Dept(self,dept_name,dept_id):

        # instance variable
        self.dept_name=dept_name
        self.dept_id=dept_id

        print("Company name Is : ", self.company_name)
        print("Company Department Details :  ",self.dept_name,"  ", self.dept_id)
    
c1=Company()
print(c1.company_name)

d1=c1.Dept("IT",123)


##############################################

# __init__ - constrcutor is a special type of methods or fucntion which is used to intialize or set instanceof a class 
# automatically invoked
# used to defined common class properties/attributes

# def __init__(self):
    # pass

class Car:
    # class varaible
    car_brand="Honda"

# defined constructor
    def __init__(self,name,color,model):
        # instance variables
        self.name=name
        self.color=color
        self.model=model
        print(f"Car setails. {self.name} and {self.color} {self.model} and Company Brand. {self.car_brand}" )

    def start(self):
        print("Car start...")
    


c1=Car("Honda CIvic","Black","S+")
c2=Car("Hyundai Verna","White","S+")
c3=Car("Hyundai Creata","Black","S")

c3.start()

# now no need to call method each and every time

# c1.CarDetails("Honda Elantra","Black","S+")
# c1.CarDetails("Honda CIVIC","White","S")

        

        