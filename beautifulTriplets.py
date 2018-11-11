def beautifulTriplets(d, arr):
  result = 0
  
  for i in arr:
    if i + d in arr and i + 2*d in arr:
      result += 1
      print(i, i+d, i+2*d)
  return result

#print(beautifulTriplets(1, [2, 2, 3, 4, 5]))
print(beautifulTriplets(3, [1, 2, 4, 5, 7, 8, 10]))

