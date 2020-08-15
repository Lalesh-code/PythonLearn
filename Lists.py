#List are similar to arrays - Mutable. Sequesnce type is define in lists. Symbol = [List]

list1 =list()
print(list1)  # empty list

list2=list([1,5,10,15,20])
print(list2) # [1,5,10,15,20]

list3=list(["tom","jerry"])
print(list3) # ['tom', 'jerry']

list4 = [1,10,100,200,300,500]
print(list4[1:4]) # [10, 100, 200] - index 1,2,3 only
print(2 in list4) # false
print(500 in list4) # true
print(2 not in list4) # true
print(500 not in list4) # false
print(len(list4)) #6
print(max(list4)) #500
print(min(list4)) #1
print(sum(list4)) # 1111
print(list4[0:5]) # [1, 10, 100, 200, 300]
print(list4[:4]) # [1, 10, 100, 200]
print(list4[2:]) # [100, 200, 300, 500]
print(list4[2:5:1]) # [100, 200, 300]
print(list4[0:6:2]) # [1, 100, 300]

# + and * Operators:
list5=[11,22,33]
list6=[44,55]
print(list5+list6) # [11, 22, 33, 44, 55]

list7=[1,2]
print(list7*3) # [1, 2, 1, 2, 1, 2]

list8=[1,2,3,4,5]
for i in list8:
    print(i) # 1 2 3 4 5 one after another o second line

# to disploy the o/p on same line
#    print(i, end=" ") # 1 2 3 4 5

list9 = [2,4,6,8,10]
list9.append(12)
print(list9) # [2, 4, 6, 8, 10, 12]

print(list9.count(8)) #1

list9.extend(list8)
print(list9) # [2, 4, 6, 8, 10, 12, 1, 2, 3, 4, 5]

print(list9.index(12)) #5

list9.insert(3,200)
print(list9) # [2, 4, 6, 200, 8, 10, 12, 1, 2, 3, 4, 5] - at index positio 3, 200 is added

print(list9.pop(2)) # 6 is returned for 3rd index position and removed.

print(list9) # [2, 4, 200, 8, 10, 12, 1, 2, 3, 4, 5] - now 6 removed from list

list9.remove(3)
print(list9)  # [2, 4, 200, 8, 10, 12, 1, 2, 4, 5]

list9.reverse()
print(list9) # reverse the list order - [5, 4, 2, 1, 12, 10, 8, 200, 4, 2]

list9.sort()
print(list9) # sort ode - [1, 2, 2, 4, 4, 5, 8, 10, 12, 200]















