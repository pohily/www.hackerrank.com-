def countingSort(arr):
    count = [0*i for i in range(100)]
    for elem in arr:
        count[elem] += 1
    sorted_arr = []
    for index in range(100):
        if count[index] != 0:
            for i in range(count[index]):
                sorted_arr.append(index)
    return sorted_arr
print(countingSort([63, 25, 73, 1, 98]))
