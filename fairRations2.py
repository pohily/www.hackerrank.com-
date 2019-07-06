def fairRations(B):
    back = list(reversed(B))
    odd = [x for x in B if x % 2 == 1]
  
    if len(odd) % 2 == 1:
        return "NO"
    else:
        count = 0
        count2 = 0
        for index, value in enumerate(B):
            if value % 2 == 1:
                B[index + 1] += 1
                count += 2
        for index, value in enumerate(back):
            if value % 2 == 1:
                back[index + 1] += 1
                count2 += 2
    return min(count2, count)

  

print(fairRations([2, 3, 4, 5, 6]))

    
    

