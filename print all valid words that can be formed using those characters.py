d = ["go", "bat", "me", "eat", "goal", "boy", "run"]
ch = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
c1 = set(ch)
res = [w for w in d if set(w).issubset(c1)]
print(res)



d = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
ch = ['e', 'o', 'b', 'a', 'm', 'g', 'l']

for word in d:
    valid = True
    for c in word:
        if c not in ch or word.count(c) > ch.count(c):
            valid = False
            break
    if valid:
        print(word)
