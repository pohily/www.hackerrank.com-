def cavityMap(grid):
  r = []
  c = []
  for row in range(1, len(grid)-1):
    for col in range(1, len(grid)-1):
      if int(grid[row][col]) > int(grid[row-1][col]) and int(grid[row][col])> int(grid[row+1][col]) and int(grid[row][col])> int(grid[row][col-1]) and int(grid[row][col])> int(grid[row][col+1]):
        r.append(row)
        c.append(col)
  #make new grid
  for i in range(len(r)):
    tmp = grid[r[i]][:c[i]] + "X" + grid[r[i]][c[i]+1:]
    grid.insert(r[i], tmp)
    grid.pop(r[i]+1)
  # print result
  for row in range(len(grid)):
    print(grid[row])
    print()
  return grid

cavityMap(["1112", "1912", "1892", "1234"])
