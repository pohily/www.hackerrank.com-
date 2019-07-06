def weightedUniformStrings(s, queries):
    result = []
    substrings = []
    subs = []
    stack = []
    
    # cut in uniforms
    stack.append(0)
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            subs.append(s[stack.pop():i])
            stack.append(i)
    if stack != []:
        subs.append(s[stack.pop():len(s)])
   
    # find all the sub strings
    for sub in subs:
        for i in range(len(sub)):
            substrings.append((i+1)*(ord(sub[i])-96))

    # check the queries
    for q in queries:
        
        if q in substrings:
            result.append('Yes')
        else:
            result.append('No')
    return result




print(weightedUniformStrings('abccddde', [1, 3, 12, 5, 9, 10]))
