def findDigits(n):
  str_n = str(n)
  digits = 0
  for i in str_n:
    if int(i) != 0 and n % int(i) == 0:
      digits += 1
  return digits

print(findDigits(1012))



