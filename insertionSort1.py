def insertionSort1(n, arr):
    tmp = arr[n-1]
    arr[n-1] = arr[n-2]
    for i in arr:
        print(i, end=" ")
    print()
    for i in range(2, n):
        if arr[n-i-1] > tmp:
            arr[n-i] = arr[n-i-1]
            for i in arr:
                print(i, end=" ")
            print()
        else:
            arr[n-i] = tmp
            for i in arr:
                print(i, end=" ")
            print()
            break
    if arr[0] > tmp:
        arr[0] = tmp
        for i in arr:
            print(i, end=" ")
        print()
insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
