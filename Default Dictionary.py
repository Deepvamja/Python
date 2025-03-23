from collections import defaultdict

# Create a defaultdict with a default
# value of an empty list
d = defaultdict(list)

# Add elements to the defaultdict and print it
d['fruits'].append('apple')
d['vegetables'].append('carrot')
print(d)

# No key error raised here and an empty list
# is printed
print(d['juices'])
