s = "geeksforgeeks"
sub = "geeks"

while True:
    ind = s.find(sub)    
    if ind == -1:         
        break
    s = s[:ind] + s[ind + len(sub):]   

res = (s == "")
print(res)
