def solve(names):
  preffix = []   

  for name in names:
    changed = False
    
    for letter in range(1, (len(name) + 1)):
      if name[:letter] not in preffix and changed == False:
        preffix.append(name[:letter])
        changed = True
          
    if name not in preffix and changed == False:
      preffix.append(name)
      changed = True
    
    else:
      for i in range(1, len(names)):
        if (name + str(i)) not in preffix and changed == False:
          preffix.append(name + str(i))
          changed = True  
            

  return preffix

print(solve(['alvin', 'alice', 'alvin']))
#print(solve(['mary', 'stacey', 'sam', 'samuel', 'sam', 'miguel']))



