def squares(a, b):
  from math import sqrt, ceil, floor
  #sq = 0
  #if ceil(sqrt(a)) == sqrt(a):
   # sq += 1
  #if floor(sqrt(b)) == sqrt(b):
   # sq +=1

  return len(list(range(ceil(sqrt(a)), 1+floor(sqrt(b)))))

print(squares(17, 24))
