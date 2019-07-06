def beautifulPairs(A, B):
    # find duplicates in B to find what element to change 
    # for every duplicate element from B find if it is in A, if so
    toChange = []
    B_sort = sorted(B)
    x = B_sort[0]
    for elem in B_sort[1:]:
        if elem == x:
            if elem in A:
                toChange.append(elem)
        else:
            x = elem
    print("toChange", toChange)
    # find dups in A, find dup in A with max appearances, if it's not in B than
    A_sort = sorted(A)
    dupA = []
    x = A_sort[0]
    for elem in A_sort[1:]:
        if elem == x:
            if elem in A and elem not in toChange:
                dupA.append(elem)
        else:
            x = elem
   
    # change duplicate in B for max dup in A
    
    if dupA:
        quan = [0]*(max(dupA)+1)
        for i in dupA:
            quan[i] += 1
        
        for i, v in enumerate(quan):
            if v !=0:
                if v not in B:
                    B[B.index(toChange[0])] = i
                    
                
                
    else:
        ok = False
        for change in toChange:
            if ok == True:
                break
            for elem in A:
                if elem not in B:
                    B[B.index(change)] = elem
                    toChange.remove(change)
                    ok  = True
                    break
    
    # find number of pairs
    print("A", A)
    print("B", B)
    count = 0
    for v in A:
        if v in B:
            count += 1

    return count

print(beautifulPairs([3, 5, 7, 11, 5, 8], [5, 7, 11, 10, 5, 8]))

