def flatlandSpaceStations(n, c):
    #return max([min([abs(i-j) for j in c ]) for i in range(n)])
    c.sort()
    result = []
    
    
    if c[-1] != n -1:
        result.append(n-1 - c[-1])

    if c[0] != 0:
        result.append(c[0])
        
    
    
    if len(c) > 1:
        first = c[0]
        for i in c[1:]:
            if i - first == 1:
                result.append(0)
                first = i
            else:
                result.append(((i - first))//2)
                first = i
    elif len(c) == 1:
        if c == [n-1] and n > 1:
            result.append(n-1)
        elif c == [0] and n > 1:
            result.append(n-1)
        else:
            result.append(max(c[0], n-1-c[0]))
    
    return max(result)
print(flatlandSpaceStations(5, [0, 4]))




