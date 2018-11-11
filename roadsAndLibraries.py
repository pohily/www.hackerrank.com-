def roadsAndLibraries(n, c_lib, c_road, cities):
  
  # divide by groups

  start  = True
  groups = []
  tmp = []
  forDel = []
  while cities:
    for i in cities:
      if i[0] in tmp or i[1] in tmp or start == True:
        tmp.append(i[0])
        tmp.append(i[1])
        start = False
        forDel.append(i)
    groups.append(tmp[:])
    for i in forDel:
      cities.remove(i)
    if cities:
      forDel = []
      tmp = []
      start = True
  print(groups)

  # find min quantity of roads in group
  
  #for i in groups:
    

  # compare cost of library in each city and sum of min quantity of roads and one library per group. for every group

roadsAndLibraries(6, 2, 5, [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]])
