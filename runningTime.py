def runningTime(arr):
    time = 0
    index = 1
    n = len(arr)
    
    while index < n:
        for i in reversed(range(index)):
            if arr[i+1] < arr[i]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
                time += 1
        index += 1
        
    print(time)

runningTime([2, 1, 3, 1, 2])
