# Abstraction- hiding data complexity
# used for enhance security
# abc- module allowes us to create abstract base class

# ABC- Abstract base class 

# @abstractmethod- is a decorator - 
# This method must be overridden in the child class.
# abstractmethod → to force child classes to implement certain methods



from abc import ABC, abstractmethod
# parent class
class Car(ABC):

    def details(self,_brand,color,price):
        self._brand=_brand
        self.color=color
        self.price=price

        print(f"Brand = {self._brand} , Color = {self.color} and Price ={self.price}")


    @abstractmethod
    def start(self):
        print("Car Start.....logical part")

# child class
class tesla(Car):
    def carDetails(self,_brand,color,price):
        self.details(_brand,color,price)
    
    # must be call
    def start(self):
        print("tesla is car started....")
      
    
tesla1=tesla()
tesla1.start()
tesla1.carDetails("Tesla","White","$92,223")

# cant craete instance of a abstract class


# eg 
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark Bark....")

class Cat(Animal):
    def sound(self):
        print("Meow Meow....")

Dog().sound()
Cat().sound()



from abc import ABC , abstractmethod
class car :
    def start (self):
        print("Start the car in super class.....")

class BMW(car):
    def start(self):
        print("BMW start....")
        super().start()

class Audi(car):
    def start(self):
        print("Audi start....")
        super().start()
        


bmw=BMW()
audi=Audi()
bmw.start()
audi.start()