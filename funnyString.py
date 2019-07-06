def funnyString(s):
    anti_s = s[::-1]
    dif1 = []
    dif2 = []
    for i in range(1, len(s)):
        dif1.append(abs(ord(s[i-1]) - ord(s[i])))
    for i in range(1, len(s)):
        dif2.append(abs(ord(anti_s[i-1]) - ord(anti_s[i])))
    if dif1 == dif2:
        return "Funny"
    else:
        return "Not Funny"

print(funnyString('acxz'))
print(funnyString('bcxz'))
