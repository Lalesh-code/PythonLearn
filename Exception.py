# Exception is the abnormal condition which disrupt the normal flow of the program.
# Error is the programmatic issue but exception is logical issue.
# try, except, else, finally - Keywords

# example1:
print("Program started")

try:
    print(10/0)
except ZeroDivisionError:
    print("Exception handeled")

    print("Program completed")
else:
    print("Enter in else blocked")

finally:
    print("Enter in finally block")

# Raising exception:

def enterage(age):
    if age<0:
        raise ValueError("Only +ve integer are allowed")
    if age%2==0:
        print("age is even")
    else:
        print("age is odd")

try:
    num=0
    enterage(num)
except ValueError:
    print("Only +ve integers are allowed")
except:
    print("something is wrong")








