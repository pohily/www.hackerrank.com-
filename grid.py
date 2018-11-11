def gridChallenge(grid):
  flag = "NO"

  for i in range(len(grid)):
    grid[i] = sorted(grid[i])
  

  for i in range(len(grid)-1):
    if ord(grid[i+1][0]) >= ord(grid[i][-1]):
      flag = "YES"
    else:
      flag = "NO"

  return flag
  
print(gridChallenge([["e", "b", "a", "c", "d"], ["f", "g", "h", "i", "j"], ["o", "l", "m", "k", "n"], ["t", "r", "p", "q", "s"], ["x", "y", "w", "u", "v"]]))

  
