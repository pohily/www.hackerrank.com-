def beautifulDays(i, j, k):
  beau = 0
  for i in range (i, j+1):
    if (i - int(str(i)[::-1])) % k == 0:
      beau +=1

  return beau

print(beautifulDays(20, 23, 6))