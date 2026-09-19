s= 'geeksforgeeks_is_best'
res = ''.join(word.capitalize() for word in s.split('_'))
print(res)


s = 'geeksforgeeks_is_best'
res = s.replace("_", " ").title().replace(" ", "")
print(res)
