def cutTheSticks(arr):
  result = [len(arr)]
  stock = []
  while arr:
    
    for i in arr:
      if i - min(arr) > 0:
        stock.append(i - min(arr))
    if len(stock) != 0:
      result.append(len(stock))
    arr = stock
    stock = []
  return result
print(cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]))
#print(cutTheSticks([5, 4, 4, 2, 2, 8]))
