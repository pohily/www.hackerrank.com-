def lilysHomework(arr):
    sorted_arr = sorted(arr)
    key_arr = dict(zip(sorted_arr, range(len(arr))))
    rounds = 0
    swap = 0
    while arr != sorted_arr:
        for key, value in key_arr.items():
            if arr[value] != key:
                tmp = arr[key_arr[arr[value]]]
                arr[key_arr[arr[value]]] = arr[value]
                arr[value] = tmp
                swap += 1
        rounds += 1
    print(arr)
    print("r ", rounds, " s ", swap)





print(lilysHomework([3, 4, 2, 5, 1]))
#print(lilysHomework([2, 5, 3, 1]))
#print(lilysHomework([22, 6, 8, 12, 7, 21, 14, 2, 5, 3, 1]))
