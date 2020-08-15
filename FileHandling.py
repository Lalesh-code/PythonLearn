# Read and write data to and from a file.
# Operations - Opening, closing, writing data, reading data, appending data, Looping through loops
# Modes = r - read only, w - write, a - append data at the end of file.

# Write data:
file=open('E:\SeleniumDemo\myfile.txt','w') # Open file for writing
file.write("This is first line \n")
file.write("This is second line \n")
file.close()

# Read data:
file=open('E:\SeleniumDemo\myfile.txt','r')
#print(file.read()) # read content of mytext.file - first and second line
#print(file.read(10)) # read number of characters
print(file.readline()) # This is first line
#print(file.readlines()) # ['This is first line \n', 'This is second line \n']
file.close()

# Appending data:
file=open('E:\SeleniumDemo\myfile.txt','a')
file.write("This is third line \n")
file.write("This is forth line")
file.close()

# Looping data:
file=open('E:\SeleniumDemo\myfile.txt','r')
for l in file:
    print(l)
file.close()


