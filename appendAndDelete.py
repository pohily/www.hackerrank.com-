def appendAndDelete(s, t, k):
  # compare
  compare = 0
  if len(s) <= len(t):
    for i in range(len(s)):
    
      if s[i] == t[i]:
        compare += 1
      else: 
        break
  else:
    for i in range(len(t)):
    
      if s[i] == t[i]:
        compare += 1
      else: 
        break

  # find possibility 
  min_change = len(s) - compare + (len(t) - compare)
  print(min_change)
  print(compare)
 
  if min_change > k:
    print("No")
    return "No"
  elif ((k - min_change) % 2 != 0) and (k - min_change) <= compare:
    print("No")
    return "No"
  elif ((k - min_change) % 2 != 0) and (k - min_change - compare) < compare:
    print("No")
    return "No"
  else:
    print("Yes")
    return "Yes"


appendAndDelete("abcd", "abcdert", 10)
#appendAndDelete("yu", "y", 2)

