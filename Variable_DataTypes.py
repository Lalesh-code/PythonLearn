# Variables are used to store data. Reserved memory gets allocated to variable to store the data.
# Every variable should have some type. For e.g. a-10 [a is variable and 10 is value of variable to store in memory]
# Data Types - Numbers, Strings, Tuples, List, Dictioaries, Set or Boolean - Numbers, Strings and Tuples are IMMUTABLE and List, Set and Dictionaries are MUTABLE.

a,b,name,c,s = 100,10.55, 'Lalesh',10+5j, True # Integer, float, string ['' or ""], complex, Boolean
print(a,b,name,c) # 100 10.55 Lalesh
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(name)) # <class 'str'>
print(type(c))  #<class 'complex'>
print(type(s))  # <class 'bool'>

a=b=c=10
print(a,b,c) # 10 10 10

#Swapping
x=22
y=55
y,x=x,y
print(x,y) # 55 22

# Concatenation - + operator [happens with same type numbers, integers or complex & boolean but cannot num+strings]
print(10+10) # 20
print(10.5+10.5) # 21
print('Welcome' + "Python") # WelcomePython
print(20+10.5) # 30.5
print(True+5) # 6 as True=1
print(False+15) # 15 as False=0
print(True+True) # 2 as True=1
print(False+False) # 0 as False=0
#print(10+"Welcome")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Swap,Redeclare,Delete variables
x=10
y=20
y,x=x,y
print(x,y) #20,10

# Redeclaring is possible in Python but not in Java
a=10
print(a)
a=22
print(a)

# Deleting - del operator
a=55
print(a)
del(a)
#print(a) #NameError: name 'a' is not defined

# Input function from users: input(), it takes only String value i.e '' or ""
num1 = input("Enter a first number")
num2 = input("Enter a second number")
print(num1,num2) # 10 20

print(num1+num2) # still o/p is 10 20 - need to do the Type Casting i.e. strings to convers in integers
# also int can be float but float cannot be int e.g. 10 can be 10.0 but 10.5 cannot be 10
num1 = int(input("First number"))
num2 = int(input("Second number"))
print(num1+num2)   # 30 (10+20)

# Formatting output - Percentile and dot operator - %d - Int, %s - Strings, %f or %g - Float
name = 'Lalesh'
age = 40
salary = 10000.50
print(name,age,salary)

#Approach 2
print("Name is:", name)
print("Age is:", age)
print("Salary is:", salary)

#Approach 3
print("Name:%s Age:%d Salary:%f"%(name,age,salary)) # Name:Lalesh, Age:40, Salary:10000.500000

#Approach 4
print("Name:{} Age:{} Salary:{}".format(name,age,salary))  #for curly braces - Name:Lalesh Age:40 Salary:10000.5

#Approach 5
print("Name:{0} Age:{1} Salary:{2}".format(name,age,salary)) # Indexing Name:Lalesh Age:40 Salary:10000.5




















