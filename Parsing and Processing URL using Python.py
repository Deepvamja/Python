import re  
s = 'https://www.geeksforgeeks.org/'

p = re.findall(r'(\w+)://', s)
print(p)

h = re.findall(r'://www.([\w\-.]+)', s)
print(h)



import re  
s = 'file://localhost:4040/abc_file'

p = re.findall(r'(\w+)://', s)
print(p)

h = re.findall(r'://([\w\-.]+)', s)
print(h)

hp = re.findall(r'://([\w\-.]+)(:(\d+))?', s)
print(hp)



import re  
s = 'http://www.example.com/index.html'
res = re.findall(r'(\w+)://([\w\-.]+)/(\w+)\.(\w+)', s)
print(res)
