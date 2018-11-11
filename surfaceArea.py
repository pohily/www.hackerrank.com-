def surfaceArea(A):
  nv = len(A) * len(A[0]) * 2
  
  l = 0
  for i in range(len(A)):
    l += A[i][0]

  r = 0
  for i in range(len(A)):
    r += A[i][-1]

  p = sum(A[-1])

  z = sum(A[0])

  s = 0
  for i in range(len(A)):
    for j in range(len(A[0])):
      if i != 0:  #up
        if A[i-1][j] < A[i][j]:
          s += (A[i][j] - A[i-1][j])

      if i != (len(A) - 1):   #down
        if A[i+1][j] < A[i][j]:
          s += (A[i][j] - A[i+1][j])

      if j != 0:   #left
        if A[i][j-1] < A[i][j]:
          s += (A[i][j] - A[i][j-1])

      if j != (len(A[0]) - 1):   #right
        if A[i][j+1] < A[i][j]:
          s += (A[i][j] - A[i][j+1])

  print("nv ", nv, " l ", l, " r ", r, " p ", p, " z ", z, " s ", s)
  return (nv+ l+ r+ p+ z+ s)

print(surfaceArea([[1, 3, 4], [2, 2, 3], [1, 2, 4]]))
