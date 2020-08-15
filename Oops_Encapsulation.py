# Encapsulation: this restrict the access to methods and variables. This can prevent the data from being get modified accidently or by security point of view. This is achived by using the private methods and variables.
# Private methods denoted by "__" sign.
# Public methods can be accessed from anywhere but Private methods is accessed only in their classes & methods.

class MyClass():
    __a=100  # valiable a is defined here as private denoted as '__'
    def display(self):
        print(self.__a) # passed here the same __a variable private one.

obj=MyClass()
obj.display() # O/p = 100

# print(MyClass.__a)   # __a private variable outsie of class cannot be accesed.  AttributeError: type object 'MyClass' has no attribute '__a'

class MyClass():
    def __display1(self):                       # Private Method
        print("This is first display method")

    def display2(self):                         # Public Method
        print("This is second display method")
        self.__display1()

obje=MyClass()
obje.display2()   # only public method is accessed here. display1 private method cannot be.

# We can access private variables outside of class indiretly using methods:

class MyClass():
    __empid=101      # Private variable

    def getempid(self,eid):
        self.__empid = eid # method to get the getempid.

    def dispempid(self):
        print(self.__empid) # method to get the dispempid.

obj=MyClass()
obj.getempid(105) # 105
obj.dispempid()   # 101

