def jumpingOnClouds(c, k):
    e = 100
    i = 0
    next = 1
    while ((i + k) % len(c)) > next and e > 0:
        next = (i + k) % len(c)
        if c[i] == 1:
            e -= 3
            print("next ", next, "i ", i, "c ", c[i], e)
        else:
            e -=1
            print("next ", next, "i ", i, "c", c[i], e)
        i = next
    next = (i + k) % len(c)
    if c[i] == 1:
        e -= 3
        print("next ", next, "i ", i, "c ", c[i], e)
    else:
        e -=1
        print("next ", next, "i ", i, "c", c[i], e)
    return e

print(jumpingOnClouds([0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 1))
#print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))
