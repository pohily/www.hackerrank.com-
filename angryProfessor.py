def angryProfessor(k, a):
  onTime = 0
  for i in a:
    if i <= 0:
      onTime += 1

  if onTime < k:
    return "YES"
  else:
    return "NO"

print(angryProfessor(3, [-1, -3, 4, 2]))
