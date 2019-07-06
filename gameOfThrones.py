def gameOfThrones(s):
    new = set(s)
    once = False
    for elem in new:
        if s.count(elem) % 2 == 1 and once == False:
            once = True
            continue
        elif s.count(elem) % 2 == 1 and once == True:
            return "NO"
    return "YES"

print(gameOfThrones('aaabbbb'))
