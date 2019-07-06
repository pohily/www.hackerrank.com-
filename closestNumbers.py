def closestNumbers(arr):
    empty = True
    arr.sort()
    pairs = []
    minim = []
    
    for i in arr:
        for j in arr:
            if i!= j and empty == True:
                pairs.append(i)
                pairs.append(j)
                minim.append(abs(i - j))
                empty = False
                continue
            if i != j and empty == False:
                x = abs(i - j)
                y = min(minim)
                if x < y:
                    minim[:] = []
                    pairs[:] = []
                    minim.append(x)
                    pairs.append(i)
                    pairs.append(j)
                if x == y and i not in pairs and j not in pairs:
                    pairs.append(i)
                    pairs.append(j)
    return pairs

print(closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]))
