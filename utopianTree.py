def utopianTree(n):
  result = 1
  if n == 0:
    return 1
    
  for i in range(1, n+1):
    if i % 2 == 0:
      result += 1
    else:
      result *= 2

  return result

print(utopianTree(5))

