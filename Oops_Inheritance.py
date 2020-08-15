# Inheritance - child class [derived class,sub-class] inherited the functionalities, properties of parent class [base class, super-class].

# Single inheritance
# Multilevel inheritance
# Hierarchical inheritance
# Multiple inheritance
# Hybrid inheritance (Multiple + Hierarchical)

# Single Inheritance:

class A():    # Parent class
    def m1(self):
        print("This is my m1 method from class A")

class B(A):    # Child class B - Inherited functions from Parent class A.
    def m2(self):
        print("This is my m2 method from class B")

aobj=A()
aobj.m1()  # Only able to access method of class A - O/p - This is my m1 method from class A

bobj=B()
bobj.m1() # Method of class A - Parent - O/P - This is my m1 method from class A
bobj.m2() # Method of class B - Child itself - O/P - This is my m2 method from class B

# Multiple Inheritance:

class A():    # Parent class
    def m1(self):
        print("This is my m1 method from class A")

class B(A):    # Child class B - Inherited functions from Parent class A.
    def m2(self):
        print("This is my m2 method from class B")

class C(B):    # Child class B - Inherited functions from Parent class A.
    def m3(self):
        print("This is my m3 method from class C")

aobj=A()
aobj.m1()  # Only able to access method of class A - O/p - This is my m1 method from class A

bobj=B()
bobj.m1() # Method of class A - Parent - O/P - This is my m1 method from class A
bobj.m2() # Method of class B - Child itself - O/P - This is my m2 method from class B

cobj=C()
cobj.m1() # Method of class A - Parent - O/P - This is my m1 method from class A
cobj.m2() # Method of class B - Child itself - O/P - This is my m2 method from class B
cobj.m3() # Method of class C - Child itself - O/P - This is my m3 method from class C

# Hierarchical Inheritance:

class A():
    x,y=10,20
    def add1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,200
    def add2(self):
        print(self.a+self.b)

class C(A):
    p,q=1000,2000
    def add3(self):
        print(self.p+self.q)

object1=A()
object1.add1() # access method of class A

object2=B()
object2.add1() # access method of class A
object2.add2() # access method of class B

object3=C()
object3.add1()  # access method of class A
object3.add3()  # access method of class C

# Multiple Inheritance:
class X():
    x,y=40,50
    def add1(self):
        print(self.x+self.y)

class Y():
    p,q=60,80
    def add2(self):
        print(self.p+self.q)

class Z(X,Y):
    i,j=90,100
    def add3(self):
        print(self.i+self.j)

object2 = X()
object2.add1()  # 90

object3 = Y()
object3.add2()  # 140

object4= Z() # 90 140 190
object4.add1() # 90
object4.add2() # 140
object4.add3() # 190






