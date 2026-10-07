def pigeonhole_sort(a):
    mi, mx = min(a), max(a)
    size = mx - mi + 1
    holes = [0] * size

    for x in a:
        assert isinstance(x, int), "Only integers allowed"
        holes[x - mi] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + mi
            i += 1

a = [8, 3, 2, 7, 4, 6, 8]
pigeonhole_sort(a)
print(a)
