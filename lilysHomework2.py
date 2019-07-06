def lilysHomework(arr):
    a = arr[:]
    sorted_arr = sorted(a)
    b = a[:]
    reversed_arr = list(reversed(b))
    key_arr = dict(zip(sorted_arr, range(len(arr))))
    key_rev = dict(zip(reversed_arr, range(len(arr))))
    swap2 = 0
    swap = 0
    
    print(a)
    print(reversed_arr)
    print(sorted_arr)
    while a != sorted_arr:
        for key, value in key_arr.items():
            if a[value] != key:
                a[key_arr[a[value]]], a[value] = a[value], a[key_arr[a[value]]] 
                print("s ", swap)
                swap += 1
       
    while arr != reversed_arr:
        for key, value in key_rev.items():
            if arr[value] != key:
                arr[key_rev[arr[value]]], arr[value] = arr[value], arr[key_rev[arr[value]]]
                swap2 += 1
                print("s2 ", swap2)
    if swap < swap2:
        return swap
    else:
        return swap2
    


#print(lilysHomework([3, 4, 2, 5, 1]))
print(lilysHomework([2, 5, 3, 1]))
#print(lilysHomework([22, 6, 8, 12, 7, 21, 14, 2, 5, 3, 1]))
