# Inheritance-

# purpose-
# used to inherit parent class/super class / base class methods and propeties in a dervied class / child class / subclass
# code reusability
# readibility

# Types of Inheritance

# Single Inheritance
# Multilevel Inhertiance
# Multiple
# Hirarchical
# Hybrid Inheritance

# single Inheritance-1 Parent- 1 Child

class Parent:

    name="Parent"

    def __init__(self):
        print("Parent Constructor called")
    
    def ParentDetails(self):
        print("Parent Class Method")


class Child(Parent):

    child_name="Child"

    def __init__(self):
        print("Child Constrcutor called")
    
    def childDetails(self):
        print("Child Method called")

c1=Child()

print(c1.child_name)

c1.childDetails()


# access parent method and properties

print(c1.name)
c1.ParentDetails()


#################################################

# Eg
# Employee->Manager
class Employee:

    def __init__(self,name,empRole,empId,empDept,empCTC):
        self.name=name
        self.empRole=empRole
        self.empId=empId
        self.empDept=empDept
        self.empCTC=empCTC

    def empDetails(self):
        print(f"Emp Id = {self.empId} \t  Emp Name = {self.name} and Emp Role = {self.empRole} and Emp Dept = {self.empDept} and Emp CTC ={self.empCTC}")

    def parent(self):
        print("hello parent class")

# child class
class Manager(Employee):
    def __init__(self,name,dept_name,empId,empRole,empCTC,empDept):
        self.name=name
        self.dept_name=dept_name
    
        # called parent class construtor
        super().__init__(name,empId,empRole,empCTC,empDept)

    def managerDetails(self):
        self.empDetails()
        print(f"Manager Name Is. {self.name} and Manager Dept : {self.dept_name}")


m1=Manager("Pratik","IT",12345,"Developer","20LPA","Admin")
m1.managerDetails()


################################################

# Parent class- Vehicle
        # Properties-vehicle_type,fuel_type,vehicle_mode
        # methods- vehicle_details() 

# child class- Car
      # properties- brand,color,model,price,fuel_type
      # methods- carDetails() / start()/ stop()

    
class Vehicle:
    #class variable
    def __init__(self,vehicle_type,vehicle_mode,fuel_type):

        # instance variable
        self.vehicle_type=vehicle_type
        self.vehicle_mode=vehicle_mode
        self.fuel_type=fuel_type

    def details(self):
        print(f"Vehicle Details.....{self.vehicle_type}")

# child

class Car(Vehicle):
    def __init__(self,name,brand,color,model,price,vehicle_type,vehicle_mode,fuel_type):
        self.name=name
        self.brand=brand
        self.color=color
        self.model=model
        self.price=price

        # call parent __init__
        super().__init__(vehicle_type,vehicle_mode,fuel_type)

    def details(self):
        # called parent details
        super().details()
        print(f"Car Details...{self.name}")
        

# c1=Car("BMW","BNY","Black","S+","50Lac")
# c2=Car("Curve","TATA","White","Top end","30LAC")
# c1.details()
# c2.details()

car1=Car("Hyrider","TATA","White","TOp","40LAC","4 Wheeler","Hybrid","Petrol")
car1.details()

############################################################################

# multilevel Inheritance
# grandparent-parent-child
# A-B-c
# eg
# mobile- Apps - Socila Media APps-

# Bank - Account - Account Types

# University- Colleges- Departments

class GrandParent:
    def gp(self):
       print("Grand parent class")

class parent(GrandParent):
    def p(self):
      print("Parent class")

class Child(parent):
    def c(self):
     print("Child class")

c1=Child()
c1.gp()
c1.p()
c1.c()

###########################################################
# gp
class Bank:
   def __init__(self,name,branch):
      self.name=name
      self.branch=branch

   def details(self):
      print(f"Bank details...{self.name} and {self.branch}")
      
# parent
class Account(Bank):
   def __init__(self,acc_no,acc_type,acc_bal,name,branch):
        self.acc_no=acc_no
        self.acc_type=acc_type
        self.acc_bal=acc_bal

        # parent constructor
        super().__init__(name,branch)

   def details(self):
      super().details()
      print(f"Account Details...{self.acc_no} {self.acc_type} {self.acc_bal}")
      

# child
# customer
class Customers(Account):
        def __init__(self,cust_name,cust_age ,acc_no, acc_type, acc_bal, name, branch):
            self.cust_name=cust_name
            self.cust_age=cust_age
            super().__init__(acc_no, acc_type, acc_bal, name, branch)
        
        def details(self):
            super().details()
            print(f"Customer Details....{self.cust_name} {self.cust_age}")
     
   
customer1=Customers("Narendra",21,"96655467558","Current","100000","Abcd","XYZ")
customer1.details()
 
     

