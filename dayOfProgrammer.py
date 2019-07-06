def dayOfProgrammer(year):
    if 1700 <= year <= 1917:
        if year % 4 == 0:
            return "12.09.%s" % year
        else:
            return "13.09.%s" % year
    elif year == 1918:
        return "26.09.%s" % year
    elif year > 1918:
        
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return "12.09.%s" % year
        else:
            return "13.09.%s" % year

