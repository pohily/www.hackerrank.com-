def closestNumbers(arr):
    arr.sort()
    result = []
    if len(arr) > 2:
        m = abs(arr[0] - arr[1])
        for i in range(2, len(arr)):
            if abs(arr[i] - arr[i-1]) < m:
                m = abs(arr[i] - arr[i-1])
        for i in range(2, len(arr)):
            if abs(arr[i] - arr[i-1]) == m:
                result.append(arr[i-1])
                result.append(arr[i])
        return result
    else:
        return arr
