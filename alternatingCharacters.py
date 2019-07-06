def alternatingCharacters(s):
    
    first = s[0]
    count = 0
    for letter in s[1:]:
        if first != letter:
            first = letter
        else:
            count += 1
    return count

