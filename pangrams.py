def pangrams(s):
    abc = list(range(65, 91)) + [32]

    for letter in s:
        if 65 <= ord(letter) <= 90 or ord(letter) == 32:
            let = ord(letter)
        elif 97 <= ord(letter) <= 122:
            let = ord(letter) - 32
        if let in abc:
            abc.remove(let)
    if abc == []:
        return 'pangram'
    else:
        return 'not pangram'

print(pangrams('We promptly judged antique ivory buckles for the next prize'))
print(pangrams('We promptly judged antique ivory buckles for the prize'))
