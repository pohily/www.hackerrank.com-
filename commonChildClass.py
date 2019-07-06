class Check():
    def __init__(self, lst):
        self.lst = list(lst)
    def differ(self, toCheck):
        check = []
        tmp1 = self.lst
        tmp2 = toCheck.lst
        for i, letter in enumerate(tmp1):
            if letter in tmp2:
                index = tmp2.index(letter)
                check.append(index)
                tmp2[index] = 2
            else:
                tmp1[i] = 1
        result = 1
        print(check)
        maxCheck = check[0]
        for i in range(1, len(check)):
            if check[i] > maxCheck:
                maxCheck = check[i]
                result += 1
        return result

def commonChild(s1, s2):
    ls1 = Check(s1)
    ls2 = Check(s2)
    print(ls1.differ(ls2))
    print(ls2.differ(ls1))
    """print(check)
    print(len(check))
    print(ls1)
    print(ls1.count(1))
    print(ls2)
    print(len(ls1))"""
    
     
    #return ls1.differ(ls2)
print(commonChild('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS',
                  'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'))
















