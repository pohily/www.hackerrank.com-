def twoPluses(grid):
  new = [list(y) for y in grid]
  

  # x - margin
  x = min(len(new), len(new[0]))
  if x % 2 == 0:
    margin = int(x/2 - 1)
  else:
    margin = int((x+1) / 2 - 1)

  # scan grid for pluses
  result = []
  
  while margin >= 0:
    
    for r in range(margin, len(new) - margin):
      for c in range(margin, len(new[0]) - margin):
        tmp = []
        for i in range(-margin, margin+1):
          for j in range(-margin, margin+1):
            tmp.append(new[r+i][c])
            tmp.append(new[r][c+j])          
        if "B" not in tmp:
          result.append((r, c, margin))
    margin -= 1    

  # look if fined pluses overlap
  # find max product
  print(result)
  result2 = []
  result3 = []
  for i in result:
    if i[2] > 0:
      result2.append(i)
  result2.append(result[-1])  
  
  for i in result2:
    for j in result2:
      if i != j:
        if j[0] == i[0] and abs(j[1] - i[1]) >= j[2] + i[2] + 1:
          
          result3.append((i[2] * 4 + 1) * (j[2] * 4 + 1))
        elif j[1] == i[1] and abs(j[0] - i[0]) >= j[2] + i[2] + 1:
          
          result3.append((i[2] * 4 + 1) * (j[2] * 4 + 1))
        elif j[0] != i[0] and j[1] != i[1] and (abs(j[0] - i[0]) > max(j[2], i[2]) or abs(j[1] - i[1]) > max(j[2], i[2])):
          
          result3.append((i[2] * 4 + 1) * (j[2] * 4 + 1))
  
 
    
  print(result3)
  return max(result3)

a =["GGGGGG", "GBBBGB", "GGGGGG", "GGBBGB", "GGGGGG"]
print(twoPluses(a))
print()
for i in a:
  print(i)
  
