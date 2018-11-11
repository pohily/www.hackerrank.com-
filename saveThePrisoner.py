def saveThePrisoner(n, m, s):
  
  if m > n:
    m = m % n
    if m == 0:
      m = n
      
  if m > n - s + 1:
    return m + s - n - 1

  return m + s - 1

print(saveThePrisoner(5, 2, 2))
