# * args allows us to pass variable number of arguments to the function:

def sum(*args):
    s = 0
    for i in args:
        s += i
    print("Sum of:", s)

sum(10, 20, 30, 40, 50, 100)

def my_three(a,b,c,d,e):
    print(a,b,c,d,e)

args=[1,2,3,4,5]
my_three(*args)

# **kwargs: Keyword arguments. ** means key and value

#example 1:

def my_three (a,b,c):
    print(a,b,c)
args={'a':'One','b':'Two','c':'Three'}
my_three(**args)

#example 2:

def my_func(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
my_func(name='tom', sport='cricket', squad='India')