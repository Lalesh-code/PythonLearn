name = 'Lalesh'
print(name)

name = "Garud"
print(name)

name = str("Welcome")
print(name)

#id function to get the memory location ID:
name1="welcome"
name2="python"
print(id(name1))  # 16157312
print(id(name2))  # 16157376

name3 = name2 + "my area"
print(id(name3)) # 15764880

# Operations on Strings: + for addition and * for multiply

str1 = "Welcome"
print(str1+" to Python")  # Welcome to Python

str2 = 'Welcome'
print(str2*3)  # WelcomeWelcomeWelcome

# Slicing or Indexing String operator:
str1 = "Welcome" # 0,1,2,3,4,5,6 - Welcome
print(str1[1:5]) # elco
print(str1[0:5]) # Welco
print(str1[:6]) # Welcom
print(str1[4:]) # ome

# ord(), chr(), len(), max(), min(), in and not in functions:
print(ord ('Z')) # A = 65, Z = 90
print(chr (65))  # 90 = Z, 65 = A
print(len(str1)) # 7
print(max(str1)) # o
print(min(str1)) # W

str2 = "Python"
print("com" in str2) # false
print("thon" in str2) # true
print("com" not in str2) # true
print("thon" not in str2) # false

# Compare Strings: (>,<,<=, >=, ==, !=)
print("tim" == "tie") # false
print("free" != "freedom") # true
print("man" >= "can") # true
print("son" <= "moon") # false
print("arrow" > "borrow") # false
print("teeth" < "tee") # false
print("abc" > "") # true

# Iterating strings:
str = "Python"
for i in str:
    print(str) # Python displayed 6 times as per 6 Python characters
    print(i) # P y t h o n - 6 characters displayed

s= "Welcome to python"
print(s.isalnum()) # false
print("Welcome".isalpha()) # true
print("2020".isdigit()) # true
print(s.islower()) # false
print("WELCOME".isupper()) # true
print(s.endswith("thon")) # true
print(s.startswith("ome")) # false
print(s.find("thon")) #13
print(s.rfind("come")) #3
print(s.count("o")) #3

















