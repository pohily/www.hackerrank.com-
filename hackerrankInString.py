def hackerrankInString(s):
    word = "hackerrank"
    position = 0
    letter_index = []
    for letter in word:
        if not letter in s[position:]:
            return 'NO'
        ind = s[position:].index(letter) + position
        letter_index.append(ind)
        position = s[position:].index(letter) + position + 1
        print("letter ", letter, "index", ind, "pos", position)
    for index in range(len(letter_index)-1):
        if letter_index[index] > letter_index[index + 1]:
            return 'NO'
    return 'YES'


print(hackerrankInString('hereiamstackerrank'))
print(hackerrankInString('hackerworld'))
