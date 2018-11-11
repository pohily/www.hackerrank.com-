def alternate(s):
  s_set = set(s)
  s_list = list(s)
  result = []
  
  for i in s_set:
    for j in s_set:
      if i != j:
        x = [letter for letter in s_list if letter == i or letter == j]
      else:
        continue
      consequtive = False
      for z in range(len(x)-1):
        if x[z] == x[z+1]:
          consequtive = True
          break

      if consequtive == False:
        result.append(len(x))
  
  if result:
      return max(result)
  else:
      return 0

print(alternate("asdcbsdcagfsdbgdfanfghbsfdab"))
