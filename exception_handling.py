a=5
b=2



try:
    print('resource open')
    print((a/b))
    k = int(input("enter the number"))
    print(k)
   


except Exception as e:
    print('you cannot divide a number by zero',e)

except ValueError as e:
     print('invalid input')

except Exception as e:
     print("you got something wrong!")

finally:
        print('resource close')

#finally block will be executed if we get error as well as if we don't get the error



