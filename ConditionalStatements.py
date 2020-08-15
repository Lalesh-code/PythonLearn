# Conditional statements - if,else,elif with Iterative loops and Jumping or Transfer statements

a=40
if a>20:
    print("True condition")
else:
    print("False condition")  # a=40 - True condition and a=10 - False condition

a=10
if a%2==0:
    print("Even Number")
else:
    print("Odd number") # a=10 - Even number and a=13 - Odd number

# Multiple Statements
if False:
    print("Statement1")
    print("statement2")
else:
    print("Statement3")

print("Not part of any block")

print("Welcome") if True else print("Python") # True - Welocme and False = Python

print("Welcome") if 10<20 else print ("Python") # 10<20 - Welcome and 10>20 - Python

{print("Welcome"), print("Python")} if False else {print("Lalesh"), print("Garud")} # True = Welcome Python and False = Lalesh Garud

#elif statement:
a=50
if a==10:
    print("Ten")
elif a==20:
    print("Twenty")
elif a==30:
    print("Thirty")
else:
    print("Not listed")

# Iterative statements - FOR [Range function] and WHILE Loops - follow indexing [0,1,2.....]
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(3,8))) # [3, 4, 5, 6, 7]
print(list(range(1,10,2))) # [1, 3, 5, 7, 9]
print(list(range(0,10,2))) # [0, 2, 4, 6, 8]
print(list(range(10,1,-1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(list(range(-10,-5))) # [-10, -9, -8, -7, -6]
print(list(range(-10,-5,2))) # [-10, -8, -6]

# for loops:
for i in range(10):
    print(i)  # 0 to 9

for i in range(2,11,2):
    print(i) # 2,4,6,8,10

# while loops:
i=1
while i<=10:
    print(i)
    i=i+1   # if not mentioned then infinite loops is followed. O/p - 1 to 10

i=10
while i>=1:
    print(i)
    i=i-1 # 10 to 1

# Jumping or Transfer statements: 1) Break and 2) Continue
for i in range(1,10):
    if i==5:
        break
    print(i) # 1,2,3,4 and the break as per condition.

for i in range (1,10):
    if i==5:
        continue
    print(i) # 1,2,3,4,6,7,8,9

















