s = 'Geeksforgeeks is best for geeks and CS'
li = ["best", "CS", "for"]
k = "gfg"
res = ' '.join([k if word in li else word for word in s.split()])
print(res)
