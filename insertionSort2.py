def insertionSort2(n, arr):
    index = 1
    
    
    while index < n:
        for i in reversed(range(index)):
            if arr[i+1] < arr[i]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
        index += 1
        for i in arr:
            print(i, end=" ")
        print()

insertionSort2(6, [1, 4, 3, 5, 6, 2])
