def flatlandSpaceStations(n, c):
  results = [min(abs(i-j)) for i in range(n) for j in c]
    
  return max(results)
print(flatlandSpaceStations(5, [0, 4]))
