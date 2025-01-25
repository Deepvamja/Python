# without using lambda function
def double(x):
    return x **2


# function inside function (function pass as function)
def app(fx,value):
    return 5 + fx(value)


# lambda function is to use when you want your code to be one liner


# using lambda function
double = lambda x:x*2

cube = lambda x: x*x*x
avg = lambda x,y:(x+y) / 2 

print(double(7))
print(cube(6))
print(avg(5,5))
print(app(double,2))

print(app(lambda x: x*x,2))