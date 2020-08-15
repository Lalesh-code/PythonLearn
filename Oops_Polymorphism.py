# Polymorphism - Poly means 'many' and morph means 'forms' - e.g. on web page there are multiple buttons line round button, check button, image button (many form of buttons) but they function by OnClick() method only.
# Overriding - Parent class A having method display() extended to Child class B having same method display(). Two methods having same name but doing different tasks.
# Overloading - Define method in such a way that there are multiple ways to call it.

# Simple example of Overriding:

class Parent():
    name="Tom"

class Child(Parent):
    name="Jerry"

obj7=Child()
print(obj7.name)

# Another example:
class Bank():
    def rateofinterest(self):
        return 0

class ICICI(Bank):
    def rateofinterest(self):
        return 10.5

obj5 = ICICI()
print(obj5.rateofinterest())

# Overloading: same sayhello method behave differently for 2 parameters.
class Human():
    def sayhello(self, name=None):
        if name is not None:
            print("Hello" + name)
        else:
            print("Hello")

obj=Human()
obj.sayhello()          # name=None
obj.sayhello("Lalesh")  # name="Lalesh"

