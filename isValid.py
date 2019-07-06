def isValid(s):
    new = set(s)
    result = [] #частоты уникальных букв
    for elem in new:
        result.append(s.count(elem))
        print("elem", elem, "count", s.count(elem))
    set_res = list(set(result))#уникальные частоты
    print('set_res', set_res)
    if len(set_res) == 1:
        return 'YES'
    elif len(set_res) > 2:
        return 'NO'
    else:
        if (result.count(set_res[0]) == 1 or result.count(set_res[1]) == 1) and (abs(set_res[0] - set_res[1]) == 1 or ((set_res[0]==1 or set_res[1] == 1) and result.count(1) == 1)):
            return 'YES'
        else:
            return 'NO'
print(isValid('aaaaabc'))


