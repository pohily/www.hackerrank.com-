def maxMin(k, arr):
    arr.sort()
    result = max(arr)
    for i in range(len(arr)-k+1):
        if arr[i+k-1] - arr[i] < result:
            result = arr[i+k-1] - arr[i]
    return result





