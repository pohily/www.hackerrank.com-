def pickingNumbers(a):
    
    count = [0]*(max(a)+1)
    
    for value in a:
        count[value] += 1
    result = 0

    for i in range(1, len(count)):
        if result < count[i] + count[i-1]:
            result = count[i] + count[i-1]
    return result



      
print(pickingNumbers([4, 6, 5, 3, 3, 1]))


