# Class - entity having attributes (variables) and behaviour (methods). Class having logic and this logic is included in methods.
# for e.g. Ram and Sham are two objects. Ram and Sham having their own attributes like height, weight, colour and behaviour like walking, running, eating.
# Ram and Sham objects [physical entity] are belonging to one blueprint i.e. class, named as 'human'.
# That is under Human class - 2 objects named as Ram and Sham having different variables [attributes] and methods [behaviour]

# Variables are used to store data [value] and memory gets allocated to it. For e.g. a=10 [here is variable and 10 is the value. This value gets stroed/assigned in memory]
# Methods are the logic [class] to store the data.

# Class and Object example:

class MyClass():
    def myfunc(self):
        pass

    def display(self, name):
        print("Name is:", name)


obj = MyClass()
obj.display("Lalesh")


# Python functions and methods - functions within the class called as 'Method'. Methods are same as functions.
# if functions declared outside the class then called purely 'Functions'.

# Instance and Static methods:

class MyClass():
    def myfirst(self):  # This method inside the class MyClass so it is instance method.
        print("Instance method")

    def mysecond(self):
        print("Static method")


obj1 = MyClass()
obj1.myfirst()
obj1.mysecond()


# To declare the Static method, we have to do following change in above code:
class MyClass():
    def myfirst(self):  # This method inside the class MyClass so it is instance method.
        print("Instance method")

    @staticmethod
    def mysecond():  # This method is outside the class and also declared by annotation or keyword as '@staticmethod' so it is a Static method. Also self is removed as static.
        print("Static method")


obj1 = MyClass()
obj1.myfirst()  # Instance method is called by Object.
# obj1.mysecond()
MyClass.mysecond()  # Static method is called by Class directly.

# Global [outside class], Class [within class] and Local [within method] variables:

# Class Variable:
class MyClass():
    a,b=10,50  # Class variables as declared inside the class.
    def add(self):
        print(self.a+self.b)

    def mul(self):
        print(self.a*self.b)

obj2=MyClass()
obj2.add()
obj2.mul()

# Global, class and Local Variables:
i,j = 100,200  # Global variables - outside the class.
class MyClass():
    a,b = 40,50  # Class variables - inside the class.
    def add(self,x,y): # Local variables - inside the method.
        print(x+y)
        print(self.a+self.b)    # O/p - 45 90 300
        print(i+j)


obj4=MyClass()
obj4.add(20,25)

# Global, class and local variables with same name:
a,b = 10,20  # Global variable

class MyClass():
    a,b=100,200  # Class variables

    def add(self,a,b): # Local variables

        print(a+b)  # Local variable do not require Self. Access Local variable.
        print(self.a+self.b) # Class variable do require Self. Access class variable.
        print(globals()['a']+globals()['b']) # Global variable do not require Self. globals() keyword is used if global and loca variable names are same.


obj5=MyClass()
obj5.add(1000,2000)    # 3000 300 30 output.

# Multiple Objects: One class can have multiple objects.

class MyClass():

    def display(self):
        print("Good Morning!")

obj6=MyClass()   # This are named objects and having reference variables.
obj6.display()

obj7=MyClass()
obj7.display()

# MyClass().display() - This is nameless object and no reference variable.

# Checking memory location:
class MyClass():
    def m1(self):
        pass

c1=MyClass()
c2=MyClass()

print(id(c1))   # Memory ID 7840648
print(id(c2))   # Memory ID 7840672











