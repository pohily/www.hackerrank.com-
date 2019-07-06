def palindromeIndex(s):
    change = False
    result = None
    if len(s) == 1:
        return '-1'
    if len(s) == 2:
        return '0'
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            if s[i+1] == s[-i-1]:
                result = i
                s = s[:i]+s[i+1:]
                change = True
                break
            elif s[-i-2] == s[i]:
                result = len(s)-i-1
                s = s[:len(s)-i-1]+s[len(s)-i:]
                change = True
                break
    if change == True:
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return 'NO'
    if change == False:
        return '-1'
    return result
print(palindromeIndex('hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'))



        


