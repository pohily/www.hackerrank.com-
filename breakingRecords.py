def breakingRecords(scores):
    mi = ma = scores[0]
   
    miN = maN = 0
    for i in scores[1:]:
        
        if i > ma:
            ma = i
            maN += 1
            
        elif i < mi:
            mi = i
            miN +=1
            
    result = str(maN) +" "+ str(miN)
    return result

print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
