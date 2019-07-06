def makingAnagrams(s1, s2):
    result = []
    
    conc = s1+s2
    for elem in conc:
        if not elem in s1 or not elem in s2:
            result.append(1)
        #if elem in s1 and elem in s2:
        else:
            result.append(abs(s1.count(elem) - s2.count(elem)))
        
    return sum(result)

print(makingAnagrams('bugexikjevtubidpulaelsbcqlupwetzyzdvjphn', 'lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk'))
