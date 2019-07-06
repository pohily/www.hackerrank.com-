def weightedUniformStrings(s, queries):
    result = []
    stack = []
    letters = []
    quantity = []

    
    # cut in uniforms
    stack.append(0)
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            quantity.append(len(s[stack[-1]:i]))
            letters.append(ord(s[i-1])-96)
            stack.append(i)
    if stack != []:
        quantity.append(len(s) - stack[-1])
        letters.append(ord(s[-1])-96)
   
    # check the queries
    for q in queries:
        ok = False
        for index, letter in enumerate(letters):
            if q % letter == 0 and q/letter <= quantity[index]:
                result.append('Yes')
                ok = True
                break
        if ok == False:
            result.append('No')

    return result




print(weightedUniformStrings('l', [1, 12]))
