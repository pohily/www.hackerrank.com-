def hackerlandRadioTransmitters(x, k):
    result = 0
    while x:
        print(x)
        m = min(x)
        if m + k in x:
            v = set(range(m, m + 2*k + 1))
        else:
            v = set(range(m, m + k + 1))
        print('v', v)
        x = set(x) - v
        result += 1
    return result
print(hackerlandRadioTransmitters([9, 5, 4, 2, 6, 15, 12], 2))
