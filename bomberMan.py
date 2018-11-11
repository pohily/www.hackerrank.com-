def bomberMan(n, grid):
  #initialisation
  grid_new = [list(y) for y in grid]
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "O":
        grid_new[r][c] = 1
      else:
        grid_new[r][c] = 0


  # count to n seconds
  count = 0
  start = True
  while n:
    n -= 1
    count = (count + 1) % 4

    # 1 
    if count == 1:
      for r in range(len(grid_new)):
        for c in range(len(grid_new[0])):
            if grid_new[r][c] == 0 and start == False:
              grid_new[r][c] = 1
      for r in range(len(grid_new)):
        for c in range(len(grid_new[0])):
          if grid_new[r][c] == 2:
            grid_new[r][c] = 0
            if r != (len(grid_new) - 1) and grid_new[r + 1][c] != 2:
              grid_new[r + 1][c] = 0
            if r != 0 and grid_new[r - 1][c] != 2:  
              grid_new[r - 1][c] = 0
            if c != (len(grid_new[0]) - 1) and grid_new[r][c + 1] != 2:
              grid_new[r][c + 1] = 0
            if c != 0 and grid_new[r][c - 1] != 2:  
              grid_new[r][c - 1] = 0
    # 2 
    elif count == 2:
      for r in range(len(grid_new)):
        for c in range(len(grid_new[0])):
          if grid_new[r][c] == 1:
            grid_new[r][c] = 2
      for r in range(len(grid_new)):
        for c in range(len(grid_new[0])):
            if grid_new[r][c] == 0:
              grid_new[r][c] = 1
    # 3 
    elif count == 3:
      for r in range(len(grid_new)):
        for c in range(len(grid_new[0])):
          if grid_new[r][c] == 2:
            grid_new[r][c] = 0
            if r != (len(grid_new) - 1) and grid_new[r + 1][c] != 2:
              grid_new[r + 1][c] = 0
            if r != 0 and grid_new[r - 1][c] != 2:  
              grid_new[r - 1][c] = 0
            if c != (len(grid_new[0]) - 1) and grid_new[r][c + 1] != 2:
              grid_new[r][c + 1] = 0
            if c != 0 and grid_new[r][c - 1] != 2:  
              grid_new[r][c - 1] = 0
      for r in range(len(grid_new)):
        for c in range(len(grid_new[0])):
          if grid_new[r][c] == 1:
            grid_new[r][c] = 2 

    # 4
    elif count == 0:
      pass 
        
    start = False
  
  for i in grid_new:
    print(i)
    print()        
   
  # result output
  for r in range(len(grid_new)):
    for c in range(len(grid_new[0])):
      if grid_new[r][c] == 0:
        grid_new[r][c] = "."
        
      else:
        grid_new[r][c] = "O"
        
  result = []  
  for r in range(len(grid_new)):
    x = ""
    for c in range(len(grid_new[0])):
      x += grid_new[r][c] 
    result.append(x)
    print(x)
  return result

a = [".......", "...O.O.", "....O..", "..O....", "OO...OO", "OO.O..."]
#a = [".......", "...O...", "....O..", ".......", "OO.....", "OO....."]
for time in range(1, 7):
  print(time)
  b = (bomberMan(time, a))

    
    
    


