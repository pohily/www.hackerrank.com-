def arrayManipulation(n, queries):
  arr = [0*i for i in range(n)]
  for i in range(len(queries)):
    for j in range(queries[i][0]-1, queries[i][1]):
      arr[j] += queries[i][2]
    print(arr)
  return max(arr)

a = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
print(arrayManipulation(5, a))
