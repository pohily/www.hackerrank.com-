def migratoryBirds(arr):
  # 1 sort
  arr = sorted(arr)

  # 2 list of lists of appearances
  flag = 0
  view = [[i*0] for i in range(len(arr))]
  
  for i in range(1, len(arr)):
    
    if arr[i] == arr[i-1]:
      view[flag].append(arr[i])
    else:
      flag += 1

 
  # 3 find longest list elements
  result = []
  for i in view:
    result.append(len(i))
      
   
  
  return view[max(result)-1][-1]