def almostSorted(arr): 
    etalon = {}
    errors = []
    check = []
    for i, v in enumerate(sorted(arr)):
        etalon[v] = i
    #print(etalon)
    for i, v in enumerate(arr):
        if etalon[v] != i:
            errors.append(i)
            check.append(v)
    print("errors", errors)
    if len(errors) == 2:
        print('yes')
        print('swap', errors[0], errors[1])
        return
    elif len(errors) > 2:
        checkRev = check[::-1]
        keys = list(etalon.keys())
        #print(keys[errors[0]:errors[len(errors)-1]+1])
        if keys[errors[0]:errors[len(errors)-1]+1] == checkRev:
            print('yes')
            print('reverse', errors[0], errors[-1])
            return
        else:
            print('no')
            return
    else:
        print('no')
        return
#almostSorted([1, 5, 4, 3, 2, 6])
#almostSorted([4, 2])
#almostSorted([3, 1, 2])


















