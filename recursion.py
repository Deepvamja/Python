'''
 factorial(n) = n * factorial(n-1)

'''

def factorial(n):
    if ( n==1 or n==0):
        return 1
    return n * factorial(n-1)


n = int(input('enter an number:'))
print("the factorial of given number is", {factorial(n)})


# pattern

def pattern(n):
    if (n==0):
      return
    print('*' * n)
    pattern(n-1)

pattern(8)

