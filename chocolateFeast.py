def chocolateFeast(n, c, m):
  from math import floor
  num_candys = floor(n / c)
  wrapper = num_candys

  while wrapper >= m:
    change = floor(wrapper / m)
    num_candys += change
    wrapper = wrapper % m + change

  print(num_candys)
  return num_candys

chocolateFeast(6, 2, 2)

