def kaprekarNumbers(p, q):
    result = []

    for i in range(p, q+1):
        j = str(i * i)
        
        if len(j) == 1:
            if i == 1:
                result.append(i)
        else:
            len_i = len(str(i))
            r = int(j[-len_i:])
            if r == 0:
                continue
            else:
                l = int(j[:-len_i])
                if r+l == i:
                    result.append(i)
    if result:
        for number in result:
            print(number)
            
    else:
        print('INVALID RANGE')

kaprekarNumbers(400, 700)




        


