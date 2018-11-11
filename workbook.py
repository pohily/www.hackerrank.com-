def workbook(n, k, arr):
  from math import ceil
  sp = 0
  page = 1
  
  for i in range(n):
    for j in range(ceil(arr[i] / k)):
      if (k * (j + 1) + 1) <= arr[i]:
        up = k * (j + 1) + 1
      else:
        up = arr[i] + 1
      if (k * j + 1) <= page < up:
        sp += 1
        #print("sp = ", sp, "page ", page)
      page += 1
    

  print(sp)
  return sp

  

workbook(5, 3, [4, 2, 6, 1, 10])

    
      


