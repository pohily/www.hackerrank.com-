def circularArrayRotation(a, k, queries):
    k %= len(a)
    new = a[-k:] + a[:-k]
    return [new[j] for j in queries]
print(circularArrayRotation([1, 2, 3], 2, [0, 1, 2]))
