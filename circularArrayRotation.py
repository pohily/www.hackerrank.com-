def circularArrayRotation(a, k, queries):
    from collections import deque
    k %= len(a)
    d = deque(a)
    while k:
        d.appendleft(d.pop())
        k -= 1

    return [d[i] for i in queries]
print(circularArrayRotation([1, 2, 3], 2, [0, 1, 2]))