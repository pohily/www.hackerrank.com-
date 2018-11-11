def stones(n, a, b):
  return sorted(list({a*i + b*(n-1-i) for i in range(n)}))
print(stones(3, 1, 2))
print(stones(4, 10, 100))

