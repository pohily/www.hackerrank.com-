def anagram(s):
    result = 0
    if len(s) % 2 == 1: return '-1'

    s1 = sorted(list(s[:len(s)//2]))
    s2 = sorted(list(s[len(s)//2:]))
    print(s1)
    print(s2)
    if s1 == s2: return '0'

    
    diff = (set(s1) & set(s2))
    
    #print(share)
    #print(diff)
    for i in diff:
        result += min(s1.count(i), s2.count(i))
    #print(result)
    return len(s1) - result

print(anagram('xaxbbbxx'))




        


