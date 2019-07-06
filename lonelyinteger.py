def lonelyinteger(a):
    result = [0]*101
    for i in a:
        result[i] += 1
    return result.index(1)
