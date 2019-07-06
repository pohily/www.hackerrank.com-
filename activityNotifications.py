def activityNotifications(expenditure, d):
    from statistics import median
    notif = 0
    n = len(expenditure)
    if n <= d:
        return 0
    for i in range(1, n - d + 1):
        if expenditure[i+d-1] >= 2*median(expenditure[i-1 : d+i-1]):
            notif += 1
    return notif

#print(activityNotifications([10, 20, 30, 40, 50], 3))
print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
