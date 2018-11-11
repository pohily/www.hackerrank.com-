def viralAdvertising(n):
  from math import floor
  day = [5, 2]
  cumulative = [0, 2]
  for d in range (2, n+1):
    day.append(floor((day[d-1]*3)/2))
    cumulative.append(cumulative[d-1] + floor((day[d-1]*3)/2))
  
  return cumulative[n]

print(viralAdvertising(5))
