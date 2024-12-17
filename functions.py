
def avgerage():{
               
}

a = 12
b = 22
c = 9

avg = (a + b + c )/3
print(avg)

avgerage()
print('thank you')

avgerage()
print('hello world')

avgerage()


# function with arguments


# single argument

def goodDay(name):
    print('good day '+  name)

goodDay('deep')


#double argument

def Goodday(name,ending):
     print('good day '+  name)
 
     print(ending)
Goodday('vamja','thank you')


#  with return value

def Goodday(name,ending):
     print('good day '+  name)
     print(ending)
     return 'ok'

a = Goodday('vamja','thank you')
print(a)


# strip

def rem(l,word):
     n = []
     for item in l:
           if not(item == word):
             n.append(item.strip(word))
     return n
     
l = ['deep','devan','denish',"an"]

print(rem(l,"an"))




