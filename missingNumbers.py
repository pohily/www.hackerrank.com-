def missingNumbers(arr, brr):
    a = [0]*101
    b = [0]*101
    m = min(brr)
    result = []
    for value in arr:
        a[value - m] += 1
    for value in brr:
        b[value - m] += 1
    print(a)
    print(b)
    for i in range(len(b)):
        if a[i] < b[i]:
            result.append(i + m)
    return result
print(missingNumbers([7, 2, 5, 3, 5, 3], [7, 2, 5, 4, 6, 3, 5, 3]))
