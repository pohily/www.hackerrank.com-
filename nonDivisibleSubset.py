def nonDivisibleSubset(k, S):
 # первый список пар которые не делятся на к
  pair_sums = []
  
  for i in S:
      
    for j in S:
        
      if i != j and (i + j) % k != 0:
        if i not in pair_sums:
           
          pair_sums.append(i)
        elif j not in pair_sums:
            
          pair_sums.append(j)
        
  # теперь надо выбрать из нашего списка пары которые между собой не делятся  
  
  m = len(pair_sums)
  print(pair_sums)
  return m

#nonDivisibleSubset(3, [1, 7, 2, 4])
nonDivisibleSubset(4, [19, 10, 12, 10, 24, 25, 22])
