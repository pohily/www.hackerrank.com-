def superDigit(n, k):
    p = str(n) * k
    if len(p) == 1:
        return int(p)
    else:
        new_p = 0
        for letter in p:
            new_p += int(letter)
        superDigit(new_p, 1)
        return int(new_p)

print(superDigit(148, 3))
