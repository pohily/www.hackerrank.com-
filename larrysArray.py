def rotate(arr): #работает, но медленно
    arr[0], arr[1], arr[2] = arr[1], arr[2], arr[0]
    return arr
def larrysArray(A):
    count = 0
    for i in range(len(A)-2):
        nextI = A.index(i+1)
        while nextI > i + 2:            #передвигаем меньше в начало
            j = nextI - 2
            x = A[j:j+3]
            while x[0] != min(x):
                rotate(x)
            for index in range(3):
                A[j+index] = x[index]
                nextI = A.index(i+1)
            count +=1
        x = A[i:i+3]                   #сортируем начало
        while x[0] != min(x):
            rotate(x)
            #print(x)
        for index in range(3):
            A[i+index] = x[index]
        count +=1
    print(count, A)
    if A != sorted(A):
        return 'NO'
    else:
        return 'YES'

#print(larrysArray([3, 2, 1]))
#print(larrysArray([9, 6, 8, 12, 3, 7, 1, 11, 10, 2, 5, 4]))
print(larrysArray([17, 21, 2, 1, 16, 9, 12, 11, 6, 18,
                   20, 7, 14, 8, 19, 10, 3, 4, 13, 5, 15]))   
















