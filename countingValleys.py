def countingValleys(n, s):
  path = []
  
  for i in s:
    if i == "D":
      path.append(-1)
    else:
      path.append(1)


  valleys = count = 0 

  for i in path:
    count += i
    if count < 0:
      valley = True
    elif count > 0:
      valley = False
    
    elif count == 0 and valley == True:
      valleys += 1

  return valleys

print(countingValleys(8, ["D", "D", "U", "U", "U", "U", "D", "D"]))
    
      
      



