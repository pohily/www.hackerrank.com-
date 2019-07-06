def getTotalX(a, b):
    result = 0
    for i in range(max(a), min(b)+1):
        ok = True
        for A in a:
            if i % A != 0:
                ok = False
                break                
        for B in b:
            if B % i != 0:
                ok = False
                break  
        if ok == True:
            result += 1
            print("i ", i)
    
    return result

print(getTotalX([2, 4], [16, 32, 96]))
