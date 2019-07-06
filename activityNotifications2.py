def activityNotifications(expenditure, d):
    notif = 0
    sort_exped = sorted(expenditure)
    n = len(expenditure)
    med = d//2

    
    if n <= d:
        return 0

    if d % 2 == 1:
        for i in range(n - d):
            median = sort_exped[med + i]
            if expenditure[i+d] >= 2*median:
                notif += 1

    else:
        for i in range(n - d):
            median = (sort_exped[med + i - 1] + sort_exped[med + i]) / 2
            if expenditure[i+d] >= 2*median:
                notif += 1
    return notif
    
print(activityNotifications([10, 20, 30, 40, 50], 3))
#print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))


