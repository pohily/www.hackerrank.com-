def jimOrders(orders):
    times = {}
    for i, v in enumerate(orders):
        if sum(v) in times:
            times[sum(v)+1] = i + 1
        else:
            times[sum(v)] = i + 1
        
    print(times)
    k = sorted(times.keys())
    return [times[k[i]] for i in range(len(k))]
print(jimOrders([[1, 1], [1, 1]]))







