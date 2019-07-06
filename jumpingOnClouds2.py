def jumpingOnClouds(c, k):
    e = 100
    position = 1
    start = True

    while e and position:
        if start == True:
            position = 0
            start = False

        if c[position] == 0:
            e -= 1
        else:
            e -= 3

        position = (position + k) % len(c)
    return e

print(jumpingOnClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3))
#print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))
