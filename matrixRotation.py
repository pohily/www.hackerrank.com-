def matrixRotation(matrix, r):

  sh = len(matrix[0])
  dl = len(matrix)
  
  
  while r:
    margin = int(min(dl, sh) / 2 - 1)
    while margin >= 0:

      tmp = matrix[margin][margin]

      for i in range(1, sh - 2 * margin):  # right
        matrix[margin][margin + i - 1] = matrix[margin][margin + i]
        
      for i in range(1, dl - 2 * margin):  # down
        matrix[margin + i - 1][sh - margin - 1] = matrix[margin + i][sh - margin - 1]
        
      for i in range(1, sh - 2 * margin):  # left
        matrix[dl - margin - 1][sh - margin - i] = matrix[dl - margin - 1][sh - margin - 1 - i]
        
      for i in range(1, dl - 2 * margin - 1):  # up
        matrix[dl - margin - i][margin] = matrix[dl - margin - i - 1][margin]
        
      matrix[margin + 1][margin] = tmp
      margin -= 1
    r -= 1
  for i in range(dl):
    for j in range(sh):
      print(matrix[i][j], end=" ")
    print()
  return matrix
#a = [[1, 2], [3, 4]]
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#a = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
for i in a:
  print(i)
print()
matrixRotation(a, 12)
