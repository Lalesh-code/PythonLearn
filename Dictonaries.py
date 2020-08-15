# Dictionaries are mutable, cna be changed. It always have KEY-VALUE pair. Key is always unique but value van be anything.

friends ={"tom":11,
          "jerry": 99}
print(friends) # {'tom': 11, 'jerry': 99}

# Retrieving value for key:
print(friends["tom"]) # 11
print(friends['jerry']) # 99

# Adding
friends["Bob"] = 100
print(friends) # {'tom': 11, 'jerry': 99, 'Bob': 100}

# Modifying
friends["tom"] = 55
print(friends) # {'tom': 55, 'jerry': 99, 'Bob': 100}

# Looping
values = {'a':100,
          'b':200,
          'c':300,
          'd':400}
for key in values:
    print(key,":", values[key]) # a:100 b:200 c=300 d=400

print(len(values)) #4

value1 = {"Lalesh":40, "Gunjan":35}
value2 = {"Janhavi":13, "Aatmaja": 6}
print(value1) # {'Lalesh': 40, 'Gunjan': 35}
print(value2) # {'Janhavi': 13, 'Aatmaja': 6}

print(value1==value2) # false
print(value1!=value2) # true

mydict = {'a':1, 'b':5, 'c':10}
print(mydict.popitem()) # randomly select any item and removed ('c', 10)
print(mydict) # {'a': 1, 'b': 5}

print(mydict.keys()) # dict_keys(['a', 'b'])
print(mydict.values()) # dict_values([1, 5])
print(mydict.get('b')) # 5
print(mydict.pop('a')) #1 but should be popped out
print(mydict) # {'b': 5} remaining one
print(mydict.clear()) # None
print(mydict) # cleared {}










