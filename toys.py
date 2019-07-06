def toys(w):
    i = 0
    print("list", w)
    w = set(w)
    print("set", w)
    while len(w) > 0:
        i += 1
        m = min(w)
        w = w - (set(range(m, m + 5)))
        print(w)
    print(i)

        
    
             
    
print(toys([16, 18, 10, 13, 2, 9, 17 ,17, 0, 19]))


