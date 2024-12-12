# slicing

name = "hellodeep"
print(name[-5:-1])

name = "vamjadeep"
print(name[1:5])

# string functions 

name = "deep"
print(len(name))

print(name.startswith('de'))

print(name.capitalize())

# note : string is immutable the result it gives is new string

print(name)

# escape sequences

a = "hello from deep\nhow old are you"

b ="hello\tfrom\'world\'"

print(a)
print(b)

# f string 
name = input("enter your name :")

print(f"good evening {name}")


letter = '''Dear <name>,
your are selected
<date>'''

print(letter.replace('<name>',"deep").replace('<date>','27 november 2040'))
print(letter)

# note : string is immutable the result it gives is new string








