def superReducedString(s):
  reduced = True
  while reduced:
    reduced = False
    for i in range(len(s)-1):
      if s[i] == s[i+1]:
        s = s[:i] + s[i+2:]
        reduced = True
        break
        
  if s == "":
    return 'Empty String'
  else:
    return s

superReducedString("aaabccddd")
