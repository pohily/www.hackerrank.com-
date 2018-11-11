def repeatedString(s, n):
    from math import ceil
    if s == "a":
        return n
    if len(s) < n:
        new = (s * ceil(n / len(s)))[:n]
    else:
        new = s[:n]
    print(new)
    return new.count("a")

print(repeatedString("a", 1000000000))



