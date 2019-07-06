def highestValuePalindrome(s, n, k):
    # find min quantity of changes to make palindrom 
    minPalindrom = list(s) 
    nines = 0
    changes = 0
    before = 0
    for i in range(n):
        if minPalindrom[i] == '9':
            before += 1
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            changes += 1
            if s[i] < s[n-i-1]:
                minPalindrom[i] = minPalindrom[n-i-1]   #and make max palindrom
            else:                                       # for min changes
                minPalindrom[n-i-1] = minPalindrom[i]
    for i in range(n):
        if minPalindrom[i] == '9':
            nines += 1
    x = k - changes
    err_change = changes - (nines - before)
    if x <= err_change:
        x *= 2
    else:
        x = x + err_change  
        
    not_nines = n - nines
    if x >= not_nines:
        return '9'*n
        
    print('changes', changes, "x", x, "nines", nines)
    # compare it to k and make palindrom max of possible
    if k < changes:
        return '-1'
    elif k == changes:
        return ''.join(minPalindrom)
    else:
        if nines == n: 
                                                      # everything's ok already
            return ''.join(minPalindrom)
        
        else:                                            # make palindrom max
            if x % 2 == 1 and n % 2 == 1 and minPalindrom[n//2] != '9':
                minPalindrom[n//2] = '9'
                x -= 1
                not_nines -= 1
            elif x % 2 == 1 and not_nines % 2 == 0:
                x -= 1
            if x > not_nines:
                x = not_nines
            while x:
                
                for i in range(n):
                    if minPalindrom[i] != '9':
                        minPalindrom[i] = minPalindrom[-i-1] = '9'
                        x -= 2
                        break
                        
        return ''.join(minPalindrom) 

print(highestValuePalindrome('3943', 4, 1))

        


