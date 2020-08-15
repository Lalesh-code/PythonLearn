#Similar to list, symobol - () - Immutable cannot be changed.
tuple=()
print(type(tuple)) # () <class 'tuple'>

tuple1 = (11,22,33,44,55)
print(tuple1) # (11, 22, 33, 44, 55)

tuple2=[1,2,3,4,5]
print(tuple2) # [1, 2, 3, 4, 5]

tuple3= ("Welcome Tuple")
print(tuple3) # Welcome Tuple

print(max(tuple3)) # u
print(min(tuple2)) # 1
print(len(tuple3)) # 13
print(sum(tuple2)) # 15

tuple4 = (1,10,20,30,40,50)
print(tuple4) # (1, 10, 20, 30, 40, 50)

for i in tuple4:
    print(i, end=" ") # 1 10 20 30 40 50

tuple5 = [10,20,30,40,50,60,70,80]
print(tuple5[2:6]) # [30, 40, 50, 60]
print(tuple5[:5]) # [10, 20, 30, 40, 50]
print(tuple5[3:]) # [40, 50, 60, 70, 80]

print(50 in tuple5) # true
print(30 not in tuple5) # false
print(20 not in tuple5) # false
print(100 in tuple5) # false








