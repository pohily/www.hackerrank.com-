def organizingContainers(container):
    h = []
    v = []
    for i in container:
        h.append(sum(i))
    for i in range(len(container)):
        tmp = 0
        for j in container:
            tmp += j[i]
        v.append(tmp)
    h.sort()
    v.sort()
    if v == h:
        return 'Possible'
    else:
        return 'Impossible'

#print(organizingContainers([[0, 2, 1], [1, 1, 1], [2, 0, 0]]))
print(organizingContainers([[1, 3, 1], [2, 1, 2], [3, 3, 3]]))
