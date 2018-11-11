def caesarCipher(s, k):
    new = ""
    k = k % 26
    for letter in s:
        if 97 <= ord(letter) <= 122 or 65 <= ord(letter) <= 90:
            new_letter = ord(letter) + k
            if new_letter > 122:
                new_letter = new_letter % 122 + 96
            elif 90 < new_letter and 65 <= ord(letter) <= 90:
                new_letter = new_letter % 90 + 64
            
            new += chr(new_letter)

        else:
            new += letter
    return new

print(caesarCipher("!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U", 62))
            
