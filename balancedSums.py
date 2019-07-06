def balancedSums(arr):
    """for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return 'YES'
    return 'NO'"""   #в лоб


    sumL = 0
    sumR = sum(arr) - arr[0]
    if sumL == sumR:
            return 'YES'
    else:
        sumL = arr[0]
        sumR -= arr[1]
            
    for i in range(1, len(arr)-1):
        print("L", sumL, "R", sumR)
        if sumL != sumR:
            sumL += arr[i]
            sumR -= arr[i+1]
        else:
            return 'YES'
    return 'NO'

print(balancedSums([1, 2, 3, 3]))
