def check(l1, l2):
    result = []
    position = 0
    l1.append('1')
    
    while l1[position] != '1':
        
        while l1[position] != '1':
            if not l1[position+2:]:
                set2 = l2
            else:
                set2 = l2[:position+1]
            intersect = set(l1[:position+1]) & set(set2)
            if intersect:
                
                intersect = list(intersect)
                if len(intersect) != 1:
                    del intersect[0]
                result.append(intersect)
                l1 = l1[l1.index(intersect[0])+1:]
                l2 = l2[l2.index(intersect[0])+1:]
                #print(l1)
                #print(l2)
                position =0
                break
            else:
                position +=1
                
    
    
    print(result) 
    return sum([len(i) for i in result])
def commonChild(s1, s2):
    lt1 = list(s1)
    lt2 = list(s2)
    lo1 = lt1[::-1]
    lo2 = lt2[::-1]
    a1 = check(lt1, lt2)    
    a2 = check(lo1, lo2)
    
    print(a1, a2)
    return max(a1, a2)
print(commonChild('TERRACED',
                  'CRATERED'))
















