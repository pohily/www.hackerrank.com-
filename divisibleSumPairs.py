
  
def divisibleSumPairs(n, k, ar):
  result = 0
  
  #return sum(1 for i in range(n) for j in range(n) if i < j and (ar[i]+ar[j])%k == 0)
  for i in range(n):
    for j in range(n):
      if i < j and (ar[i] + ar[j]) % k == 0:
        result += 1

  return result

print(divisibleSumPairs(100, 22, [43, 95, 51, 55, 40, 86, 65, 81, 51, 20, 47, 50, 65, 53, 23, 78, 75, 75, 47, 73, 25, 27, 14, 8, 26, 58, 95, 28, 3, 23, 48, 69, 26, 3, 73, 52, 34, 7, 40, 33, 56, 98, 71, 29, 70, 71, 28, 12, 18, 49, 19, 25, 2, 18, 15, 41, 51, 42, 46, 19, 98, 56, 54, 98, 72, 25, 16, 49, 34, 99, 48, 93, 64, 44, 50, 91, 44, 17, 63, 27, 3, 65, 75, 19, 68, 30, 43, 37, 72, 54, 82, 92, 37, 52, 72, 62, 3, 88, 82, 71])) 



