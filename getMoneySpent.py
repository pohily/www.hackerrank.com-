def getMoneySpent(keyboards, drives, b):
  if min(keyboards) + min(drives) > b:
    return -1

  spent = []  
  for  i in keyboards:
    for j in drives:
      if i + j <= b:
        spent.append(i + j)

  return max(spent)

print(getMoneySpent([3, 1], [5, 2, 8], 10))
