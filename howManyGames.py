def howManyGames(p, d, m, s):
    quantity = 0
    if p <= s:
      quantity += 1
      s -=  p
    else:
      print(quantity)
      return quantity

    if (p-d) > s:
      print(quantity)
      return quantity
    
    while (p - d) <= s and p >= d and (p - d) >= m:
      quantity += 1
      p -= d
      s -= p
      
    while m <= s and p >= m:
      quantity += 1
      p = m
      s -= m
      

    print(quantity)  
    return quantity

howManyGames(100, 19, 1, 180)
