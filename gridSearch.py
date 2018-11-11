def gridSearch(G, P):
  line = []
  index = []
  quantity = 0
  checking = []
  #ищем вхождения
  for i in range(len(G)):
    if P[0] in G[i]:
      line.append(i)
      index.append(G[i].index(P[0]))
      quantity += 1
  if quantity == 0:
    print("NO")
    return "NO"
  # на каждое вхождение первой строки проверяем вхождение остальных по тому же индексу на строках ниже
  for i in range(quantity):
    for j in range(1, len(P)):
      if P[j] in G[line[i]+j] and G[line[i]+j].index(P[j]) == index[i]:
        checking.append(1)  
      else:
        checking.append(0)  
  tmp = "1"
  for i in checking:
    tmp += str(i)
  tmp2 = "1"*len(P)
  print(checking)

  if tmp2 in tmp:
    print("YES")
    return "YES"
  else:
    print("NO")
    return "NO"



gridSearch(["400453592126560", 
'114213133098692', 
'474386082879648', 
'522356951189169', 
'887109450487496', 
'992802633388782', 
'992771484966748', 
'075975207693780', 
'991799789562806', 
'404007454272504', 
'999043809916080', 
'992410809534811', 
'445893523733475', 
'768705303214174', 
'650629270887160'], ["99", "99"])
