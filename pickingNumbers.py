def pickingNumbers(a):
  a = sorted(a)

  # список уникальных чисел и их вхождений
  num = a[0]
  unic=[] # для каждого уникального числа
  q=0
  quan  = [] #количество чисел
  for i in range(len(a)):
    if a[i] == num:
      q += 1
    else:
      unic.append(a[i-1])
      quan.append(q)
      num = a[i]
      q = 1
  unic.append(a[-1])
  quan.append(q)

  print(unic)
  print(quan)

  result = []
  if len(unic) == 1:
    return 0
  
  for i in range(len(unic)-1):
    
    if abs(unic[i] - unic[i+1]) == 1:
      
      result.append(quan[i] + quan[i+1])
  print(result)
  return max(result)


      
print(pickingNumbers([1, 1, 1, 1, 1, 1, 1, 1, 1]))


