def candies(n, arr):
    curAmount = 1
    candie = [1]
    current = 0
    startHill = False
    for i in range(1, n):
        if candie[-1] < 1:
            count = 0
            candie[-1-count] = 1 + count
            while current-1-count >=0 and arr[current-1-count] >= arr[current-count]:
                count += 1
                candie[-1-count] = 1 + count
        if arr[i] < arr[current]:
            if current == 0:
                startHill = True
            curAmount -= 1
            candie.append(curAmount)
            current += 1
            continue
        elif arr[i] == arr[current]:
            if candie[-1] == 1:
                curAmount = 1
            else:
                curAmount -= 1
            candie.append(curAmount)
            current += 1
            continue
        elif arr[i] > arr[current]:
            if startHill == True and i > 1 and arr[current-1] > arr[current]: # старт с горки
                startHill = False
                count = 0
                candie[-1-count] = 1 + count
                while current-1-count >=0 and arr[current-1-count] >= arr[current-count]:
                    count += 1
                    candie[-1-count] = 1 + count
                curAmount = 2
                candie.append(curAmount)
                current += 1
                continue
            elif i > 1 and arr[current-1] > arr[current]: # дно в середине
                count = 0
                while current-1-count >=0 and arr[current-1-count] >= arr[current-count]:
                    candie[-1-count] = 1 + count
                    count += 1
                curAmount = 2
                candie.append(curAmount)
                current += 1
                continue
            else:
                curAmount += 1
                candie.append(curAmount)
                current += 1
                continue
    if candie[-1] != 1 and arr[-2] > arr[-1]: # дно в конце
        count = 0
        while i-1-count >= 0 and arr[i-1-count] >= arr[i-count]:
            candie[-1-count] = 1 + count
            count += 1
    print(candie)
    return sum(candie)
#print(candies(10, [9, 2, 3, 6, 5, 4, 3, 2,2,2]))
a = []
with open('data', 'r') as f:
    for line in f:
        a.append(int(line))

print(candies(16387, a))





