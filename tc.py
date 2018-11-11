def timeConversion(s):
    half = s[-2:]
    delta = 12
    hours = s[:2]
    if half == "AM":
        if hours == "12":
            delta = -12
        else:
            delta = 0
    if half == "PM" and hours == "12":
        delta = 0
    hours = str(int(s[:2])+delta)
    if len(hours) == 1:
        hours = "0" + hours
    return (hours + s[2:-2])

print(timeConversion("12:40:22AM"))

