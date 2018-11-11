def happyLadybugs(b):
  #каждого цвета должно быть <1 or >1 - сортировка и подсчет каждого цвета
  #если не все цвета счастливы то должна быть хотя бы одна пустая клетка

  list_b = [x for x in b]
  
  blank = False
  happy = True
  double = False
  
  for i in list_b:
    if i == "_":
      blank = True
    elif i != "_" and list_b.count(i) == 1:
        return "NO"


  first = list_b[0]
  list_b = list_b[1:]
  while list_b:
    if first == "_":
      first = list_b[0]
      list_b = list_b[1:]
      continue
    elif first != list_b[0] and happy == True:
      first = list_b[0]
      list_b = list_b[1:]
      happy = False
      continue
    elif first != list_b[0] and happy == False:
      first = list_b[0]
      list_b = list_b[1:]
      double = True
      continue
    elif first == list_b[0]:
      happy = True
      first = list_b[0]
      list_b = list_b[1:]
      continue
      
  if double == True and blank == False:
    return "NO"
  else:
    return "YES"

print(happyLadybugs("B_RRBR"))
      




  
