def boardCutting(cost_y, cost_x):
    y = 1
    x = 1
    cost_y = sorted(cost_y, reverse=True)
    cost_x = sorted(cost_x, reverse=True)
    cost = 0
    while cost_y and cost_x:
        if cost_y[0] > cost_x[0]:
            cost += cost_y[0] * y
            x += 1
            del(cost_y[0])
        else:
            cost += cost_x[0] * x
            y += 1
            del(cost_x[0])
    if cost_x:
        while cost_x:
            cost += cost_x[0] * x
            del(cost_x[0])
    else:
        while cost_y:
            cost += cost_y[0] * y
            del(cost_y[0])
    return cost % (1000000007)

print(boardCutting([2, 1, 3, 1, 4], [4, 1, 2]))
