li = [10, 20, 30]
it = iter(li)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of iteration")
        break
