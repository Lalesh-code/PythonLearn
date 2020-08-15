# Abstract - contains one or more abstract methods. A abstract method is a method that is declared but no implementation.
# Abstract class cannot be instantiated and require subclass to provide implementation for the abstract ethod.
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def display(self):
        None

class B(A):
    def display(self):
        print("This is method implementation")

obj=B()
obj.display()

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("eat non-veg")

class Cow(Animal):
    def eat(self):
        print("eat veg")

obj1=Tiger()
obj1.eat()

obj2=Cow()
obj2.eat()


# Abstract methods to call i.e. m1 and m2 both.

class X(ABC):      # abstract class
    @abstractmethod
    def m1(self):   # abstract method1
        pass

    @abstractmethod
    def m2(self):  # abstract method2
        pass

class Y(X):
    def m1(self):
        print("This is m1")

class Z(Y):
    def m2(self):
        print("This is m2")

# obj1=Y()
# obj1.m1()  # TypeError: Can't instantiate abstract class Y with abstract methods m2

obj2=Z()
obj2.m1()
obj2.m2()

# Constructor:
class Cal(ABC):
    def __init__(self,value):  # constructor (__init__)
        self.value=value

    @abstractmethod
    def add(self):   # abstract method1
        pass

    @abstractmethod
    def sub(self):   # abstract method2
        pass

class C(Cal):
    def add(self):
        print(self.value+100)  # 200
    def sub(self):
        print(self.value-10)   # 90

obj=C(100)
obj.add()
obj.sub()
