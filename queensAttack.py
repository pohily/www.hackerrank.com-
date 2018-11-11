def queensAttack(n, k, r_q, c_q, obstacles):
  result = 0
  x = []
  y = []
  obst = []
  

  for i in range(0, len(obstacles), 2):
    x.append(obstacles[i])
    y.append(obstacles[i+1])
  obst = list(zip(x, y))
  if k == 0:
    obst = [(0, 0)]
  print(obst)

  ####  up
  for i in range(1, n - r_q + 1):
    if (r_q + i, c_q) not in obst:
      result += 1
    else:
      break

  print(result, "up")###  down
  for i in range(1, r_q):
    if (r_q - i, c_q) not in obst:
      result += 1
    else:
      break

  print(result, "down")###  left
  for i in range(1, c_q):
    if (r_q, c_q - i) not in obst:
      result += 1
    else:
      break

  print(result, "left")###  right
  for i in range(1, 1 + n - c_q):
    if (r_q, c_q + i) not in obst:
      result += 1
    else:
      break

  print(result, "rigth")###  up  rigth                            j - h, i = v
  for i in range(1, 1 + n - r_q):
    
    for j in range(1, 1 + n - c_q):
      if (r_q + i, c_q + j) not in obst:
        result += 1
      else:
        
        break
    break
      
    

  print(result, "up  rigth")###  down right
  br = False
  for i in range(1, r_q):
    
    for j in range(1, 1 + n - c_q):
      if (r_q - i, c_q + j) not in obst:
        result += 1
      else:
        
        break
    break

  print(result, "down right")###   down left
  br = False
  for i in range(1, r_q):
    
    for j in range(1, c_q):
      if (r_q - i, c_q - j) not in obst:
        result += 1
      else:
        
        break
    break

  print(result, "down left")###   up left
  br = False
  for i in range(1, n - r_q + 1):
    
    for j in range(1, c_q):
      if (r_q + i, c_q - j) not in obst:
        result += 1
      else:
        
        break
    break
  print(result, "up left")
  return result

#print(queensAttack(5, 3, 4, 3, [5, 5, 4, 2, 2, 3]))
#print(queensAttack(8, 1, 4, 4, [3, 5]))
print(queensAttack(8, 0, 4, 4, []))


