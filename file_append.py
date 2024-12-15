st = " hey hello from deep vamja"

f = open('myfile.txt','a')  # myfile.txt file will be formed when you run the program  

# here "a" means append mode as it will append/add string in myfile.txt file each time you run

f.write(st)

f.close()