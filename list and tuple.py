name = ["harsh","violet",False,68,"xyz"]

print(name[3])
name[3] = "devansh"

# note : list is mutable while on another end  string is immutable

print(name[3])
print(name)

name.append("ayush") 
# it will add the string at last

print(name)

list1 = [2,5,7,12,3,1]

list1.sort()
list1.insert(2,9)

print(list1)
list1.pop(2)

print(list1)

list2 = (2,3,5,6)

print(sum(list2))


# Tuple

a = (1,2,4,5,6)
print(a)

# note: Tuple is immutable 

no = a.count(4)
print(no)

i = a.index(5)
print(i)




