def palindromeIndex(s):
    change = False
    result = None
    fs = s
    ss = s[::-1]
    
    if len(s) == 1:
        return '-1'
    if len(s) == 2:
        return '0'
    for i in range(len(fs)//2):
        if fs[i] != fs[-i-1]:
            first = i
            fs = fs[:i] + fs[i+1:]
            change = True
            break
    for i in range(len(ss)//2):
        if ss[i] != ss[-i-1]:
            second = len(s) - i - 1
            ss = ss[:i] + ss[i+1:]
            change = True
            break

    if change == True:
        for i in range(len(s)//2):
            if fs[i] != fs[-i-1]:
                return second
        for i in range(len(s)//2):
            if ss[i] != ss[-i-1]:
                return first
    else:
        return '-1'
    
print(palindromeIndex('hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'))



        


