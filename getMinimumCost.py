def getMinimumCost(k, c):
    cost = sorted(c, reverse=True)
    sur = 1
    pay = 0
    if k >= len(c):
        return sum(c)
    else:
        while cost:
            pay += sum(sur * cost[:k])
            cost = cost[k:]
            sur += 1
    return pay
print(getMinimumCost(2, [2, 5, 6]))
        






