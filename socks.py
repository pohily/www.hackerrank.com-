def sockMerchant(n, ar):
  from math import floor
  ar = sorted(ar)

  

    # list of lists of appearances
  flag = 0
  pairs = [[i*0] for i in range(n)]
  
  for i in range(1, n):
    
    if ar[i] == ar[i-1]:
      pairs[flag].append(ar[i])
    else:
      flag += 1

  # number of same elements 
  result = []
  for i in pairs:
    result.append(len(i))
  
  # number of pairs
  pair = 0
  for i in result:
    pair += floor( i / 2)

  return pair

#print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
