def strangeCounter(t):
  from math import log, ceil, pow
  n = ceil(log((t / 3 + 1), 2))
  b_n = pow(2, n-1)*3
  s_pred = -3 * (1 - pow(2, n - 1))
  return int(b_n - (t - s_pred) + 1)



for i in range (10, 20):  
  print(i, " i ", strangeCounter(i))
