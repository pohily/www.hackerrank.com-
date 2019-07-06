def maximumPerimeterTriangle(sticks):
    from itertools import combinations
    longestMax = []
    longestMin = []
    comb = combinations(sticks, 3)
    
    proper = []
    perimetr = []
    for i in comb:
        a, b, c = i
        if max(a, b, c) < (a+ b+ c) - max(a, b, c):
            proper.append(sorted([a, b, c]))
    if proper == []:
        return [-1]
    for i in proper:
        a, b, c = i
        perimetr.append(a+b+c)
    maxPer = max(perimetr)
    if perimetr.count(maxPer) == 1:
        return proper[perimetr.index(maxPer)]
    elif perimetr.count(maxPer) > 1:
        
        # longest max side
        for i in proper:
            a, b, c = i
            if a+b+c == maxPer:
                longestMax.append(max(a, b, c))
                longestMin.append(min(a, b, c))
        
        lonMax = max(longestMax)
        lonMaxCount = longestMax.count(lonMax)
        if lonMaxCount == 1:
            for i in proper:
                a, b, c = i
                if a+b+c == maxPer and max(a, b, c) == lonMax:
                    return [a, b, c]
        
        # longest min side
        elif lonMaxCount > 1: 
            for i in proper:
                a, b, c = i
                if a+b+c == maxPer and max(a, b, c) == lonMax and min(a, b, c) == max(longestMin):
                    return [a, b, c] 

        
            


print(maximumPerimeterTriangle([3, 9, 2, 15, 3]))

