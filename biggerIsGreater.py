def biggerIsGreater(w):
  ordw = []
  
  result = ""

  for i in w:
    ordw.append(ord(i))

  if len(ordw) == 1:
    return "no answer"
  same = ordw[0]
  samei = False
  for i in range(1, len(ordw)):
    if ordw[i] == same:
      samei = True
  if samei == True:
    return "no answer"
    
  swap = False
  if ordw[-1] > ordw[-2]:
    a = ordw[-2]
    ordw[-2] = ordw[-1]
    ordw[-1] = a
    swap = True
  for i in range(3, len(ordw)+1):
    for j in range (2, len(ordw)+1):
      if swap == False and i != j and j > 2 and  i > j and ordw[-i] < max(ordw[-j+1:-1]):
        swap = True
        a = max(ordw[-j+1:-1])
        temp = ordw[-i:]
        ordw = ordw[:-i]
        ordw.append(a)
        temp.remove(a)
        temp = sorted(temp)
        for i in temp:
          ordw.append(i)
        break
      


  for i in ordw:
    result = result + chr(i)
    
  return result
  

       
 
      

print(biggerIsGreater("bb"))
