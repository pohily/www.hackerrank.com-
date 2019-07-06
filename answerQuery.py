
def answerQuery(l, r):
    s = 'daadabbadcabacbcccbdcccdbcccbbaadcbabbdaaaabbbdabdbbdcadaaacaadadacddabbbbbdcccbaabbbacacddbbbcbbdbd'
    from math import factorial
    s = list(s)
    s = s[l-1:r]
    print('s', s)
    quantity = [0]*27
    for letter in s:
        quantity[ord(letter)-97] += 1
    print('quantity', quantity)
    palinElems = 0
    odd = 0
    for q in quantity:
        if q % 2 == 1:
            odd += 1
        if q >= 2:
            palinElems += q//2
    print('palinElems', palinElems)
    if odd:
        result = factorial(palinElems) * odd
    else:
        result = factorial(palinElems)
    return result % 1000000007
print(answerQuery(66, 69))

