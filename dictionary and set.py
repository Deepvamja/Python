# dictionary is a key value pair

marks = {
    "deep":87,
    "rohan":90,
    "harsh":76
}
print(marks)
print(marks,type(marks))

print(marks["rohan"])

# note : dictionary is mutable

print(marks.items())

print(marks.keys())

marks.update({"deep":98})
print(marks)

print(marks.get('rohan1'))  
#  prints none


# print(marks["rohan1"])
#  prints error

d = {}
print(type(d))  # prints empty dictionary



# SETS

S = {1,6,3}

e = set()
print(type(e))  # prints empty SETS



s = {4,6,7,8,8,9}
print(s)

# note : SETS remove duplicate element

s.add(5)
print(s)

# OPERATION ON SETS

S1 = {3,4,5,6,7,}
S2 = {8,9,10,11,5,6,12}

print(S1 - S2)

#  LENGTH OF SET
print(len(S1))

# UNION OF TWO SET
print(S1.union(S2))

# INTERSECTION OF TWO SET
print(S1.intersection(S2))


# 1 == 1.0 both are same in set



