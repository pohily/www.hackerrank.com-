def separateNumbers(s):
    if len(s) == 1 or s[0] == '0': return 'NO'
    numbers = []
    razr = 1
    
    def separator(r, ost):
        while len(ost) >= 2*r:
            first = ost[:r]
            ost = ost[r:]
            
            if ost[0] == '0':
                break
                #r += 1
                #ost = s
                
                
                
        
            if first[-1] == '9' and int(first) % 9 == 0: 
                numbers.append(int(first))
                r += 1
                continue

            numbers.append(int(first))
            
        numbers.append(int(ost))

    
    separator(razr, s)
    
    #check +1
    fail = False
    for i in range(1, len(numbers)):
        if numbers[i] - 1 != numbers[i - 1]:
            fail = True
    if fail:
        razr += 1
        numbers = []
        separator(razr, s)
     
    
    if numbers == [] or len(numbers) == 1:
        return 'NO'
    else:
        #print(numbers)
        return "YES " + str(numbers[0])
    
        



    
            
    return
     

print(separateNumbers('1234'))
print(separateNumbers('91011'))
print(separateNumbers('99100'))
print(separateNumbers('101103'))
print(separateNumbers('010203'))
print(separateNumbers('13'))
print(separateNumbers('1'))


