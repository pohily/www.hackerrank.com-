def minimumAbsoluteDifference(arr):
  abs_list = []
  for i in range(len(arr)):
    for j in range(len(arr)):
      if i != j:
        
        abs_list.append(abs(arr[i]-arr[j]))
  
  return min(abs_list)

#print(minimumAbsoluteDifference([3, -7, 0]))

print(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))
