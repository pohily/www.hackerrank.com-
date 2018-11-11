def timeInWords(h, m):
  numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
  6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
  11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 
  16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
  21: "twenty one", 22: "twenty two", 23: "twenty three", 24: "twenty four",
             25: "twenty five", 26: "twenty six", 27: "twenty seven", 28: "twenty eight", 29: "twenty nine"}

  if m == 0:
    time = numbers[h] + " o' clock"
  elif 1 < m < 30 and m != 15:
    time = numbers[m] + " minutes past " + numbers[h]
  elif 30 < m < 59 and m != 45:
    time = numbers[60 - m] + " minutes to " + numbers[h+1]
  elif m == 15:
    time = "quarter past " + numbers[h]
  elif m == 30:
    time = "half past " + numbers[h]
  elif m == 45:
    time = "quarter to " + numbers[h+1]
  elif m == 1:
    time = numbers[m] + " minute past " + numbers[h]
  elif m == 59:
    time = "one minute to " + numbers[h+1]

  print (time)  
  return time

timeInWords(5, 1)
