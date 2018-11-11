def birthday(s, d, m):
  result = 0
  for i in range(len(s)-m+1):
    if sum(s[i:(m+i)]) == d:
      result +=1
  return result

#print(birthday([1, 2, 1, 3, 2], 3, 2))
print(birthday([1, 1, 1, 1, 1], 3, 2))
