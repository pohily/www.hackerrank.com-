def minimumDistances(a):
  new = list(set(a))
  print("a ", a)
  print("new", new)
  result = []
  for i in new:
    x = a.index(i)
    print("x ", x)
    if i in a[x+1:]:
      y = x + 1 + a[x+1:].index(i)
      print("y ", y)
      result.append(abs(x-y))
  print(result)
  return min(result)

print(minimumDistances([3, 2, 1, 2, 3]))
