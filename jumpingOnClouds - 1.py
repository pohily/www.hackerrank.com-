def jumpingOnClouds(c):
    current = 0
    last = len(c)-1
    result = 0
    while current != last:
        if current + 2 <= last and c[current + 2] != 1:
            current += 2
            result += 1
            continue
        elif current + 1 <= last and c[current + 1] != 1:
            current += 1
            result += 1
            continue
    return result
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
#print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))



