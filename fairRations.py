def fairRations(B):
  result = 0
  odd = [x for x in B if x % 2 == 1]
  
  if len(odd) % 2 == 1:
    return "NO"
  else:
    return len(odd) + 2*(len(B[B.index(odd[0]):B.index(odd[-1])+1])-len(odd))

print(fairRations([2, 3, 4, 5, 6]))

    
    

