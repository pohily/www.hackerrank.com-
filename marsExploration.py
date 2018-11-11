def marsExploration(s):
    
    original = "SOS" * len(s) / 3
    count = 0
    for r_letter, or_letter in zip(s, original):
        if r_letter != or_letter:
            count += 1
    return count

print(marsExploration("SOSSPSSQSSOR"))