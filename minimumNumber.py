def minimumNumber(n, password):
  numbers = "0123456789"
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  special_characters = "!@#$%^&*()-+"
  num = False
  low = False
  up = False
  sp = False
  
  for letter in password:
    if letter in numbers:
      num = True
    elif letter in lower_case:
      low = True
    elif letter in upper_case:
      up = True
    elif letter in special_characters:
      sp = True

  ok = 0
  if num == False:
    ok += 1
  if low == False:
    ok += 1
  if up == False:
    ok += 1
  if sp == False:
    ok +=1

  if n + ok < 6:
    return 6 - n
  else:
    return ok

print(minimumNumber(11, "#HackerRank"))

    
