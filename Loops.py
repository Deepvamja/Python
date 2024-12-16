# for loop

for i in range(1,5):
    print(i)

for i in range(4):
    print(i)


for i in range(1,10,2):

    print(i)  # where third parameter (2) is step size


#  for loop with else

s = "deep"

for i in s:
    print(i)

else:
    print('done')  # this is executed when the loop is exhaust


# while loop

i = 1
while(i<=6):
    print(i)
    i +=1  # or i = i + 1

# Break statement

for i in range(10):
    if(i == 8):
      break # exit the loop right now
    print(i)

# Continue statement

for i in range(12):
    if(i==8):
        continue # skip the specific iteration  
    print(i)

# Pass statement

for i in range(12):
    pass # pass statement

i=1
while(i<9):
  print(i)
  i +=1

