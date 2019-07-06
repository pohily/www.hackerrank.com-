def decentNumber(n): 
    if n % 3 == 0:
        return int(n // 3 * "555")
    if n % 3 == 1:
        if n >= 10:
            return int((n-10) // 3 * "555" + 2 * "33333") 
        else:
            return -1
    if n % 3 == 2:
        if n >= 5:
            return int((n-5) // 3 * "555" + "33333")
        else:
            return -1
    """if n % 5 == 0:
        return int(n // 5 * "33333")
    if n % 5 == 1:
        if n >= 6:
            return int("555" * 2 + (n-6) // 5 * "33333")
        else:
            return -1
    if n % 5 == 2:
        if n >= 12:
            return int("555" * 4 + (n-12) // 5 * "33333")
        else:
            return -1
    if n % 5 == 3:
        return int("555" + (n-3) // 5 * "33333")
    if n % 5 == 4:
        if n >= 9:
            return int("555" * 3 + (n-9) // 5 * "33333")
        else:
            return -1"""

print(decentNumber(1))
print(decentNumber(3))
print(decentNumber(5))
print(decentNumber(11))
