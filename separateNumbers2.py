def separateNumbers(s):
    test = ''
    if len(s) == 1 or s[0] == '0': 
        print('NO')
        return 'NO'
    for r in range(1, len(s) // 2+1):
        first = int(s[:r])
        init = str(first)
        while len(test) < len(s):
            test += str(first)
            first += 1
        
        if test == s:
            print("YES", init)
            return "YES" + init
        elif test !=s and r == len(s) // 2:
            print('NO')
            return 'NO'
        test = ''

        
     

#separateNumbers('1234')
#separateNumbers('91011')
#separateNumbers('99100')
#separateNumbers('101103')
#separateNumbers('010203')
#separateNumbers('13')
#separateNumbers('1')
print()
#separateNumbers('99910001001')
#separateNumbers('7891011')
separateNumbers('9899100')
#separateNumbers('999100010001')


