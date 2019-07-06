def maximizingXor(l, r):
    result = 0
    for i in range(l, r+1):
        for j in range(l, r+1):
            if i^j > result:
                result = i^j
    return result