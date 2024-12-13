f = open('files.txt',"r")  # here "r" means read mode
data = f.read()
print(data)
f.close()

# the same can be written using "with" statement:

with open("files.txt") as f:
    print(f.read())

# you dont have close the file explicitly that is f.close()



f = open('files.txt')

lines = f.readline()

print(lines, type(lines))

f.close()

