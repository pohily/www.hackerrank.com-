def morganAndString(a, b):
    result = ''
    while a and b:
        if a[0] < b[0]:
            result += a[0]
            a = a[1:]
            continue
        elif b[0] < a[0]:
            result += b[0]
            b = b[1:]
            continue
        else:
            if len(a) == 1 and len(b) == 1:
                result += a
                result += b
                return result
            elif len(a) == 1 and len(b) > 1:
                result += b[0]
                b = b[1:]
                continue
            elif len(a) > 1 and len(b) == 1:
                result += a[0]
                a = a[1:]
                continue
            elif len(a) > 1 and len(b) > 1:
                if a[1] > b[1]:
                    result += b[0]
                    b = b[1:]
                    continue
                elif b[1] >= a[1]:
                    result += a[0]
                    a = a[1:]
                    continue
    if a:
        result += a 
    elif b:
        result += b
    return result
print(morganAndString('ABACABA',
                      'ABACABA'))
