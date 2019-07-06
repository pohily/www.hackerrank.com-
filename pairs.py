def pairs(k, arr):
    result = 0
    for value in arr:
        if value + k in arr:
            result += 1
    return result


    #return len(set(a) & set(x + k for x in a)) #- работает быстрее 

