def pageCount(n, p):
    from math import floor, ceil
    
    # from 1

    if p % 2 == 0:
      turnsF = ceil((p - 1) / 2)                # страница четная
    else:
      turnsF = (p - 1) / 2                      # страница нечетная

    # from last

    if n % 2 != 0:                        # листов нечет
      if p % 2 != 0:                      # страница нечет
        turnsL = (n - p) / 2
      else:                               # страница чет
        turnsL = floor((n - p) / 2)
    else:                                 # листов чет
      if p % 2 != 0:                      # страница нечет
        turnsL = ceil((n - p) / 2)        
      else:                               # страница чет
        turnsL = ((n - p) / 2)

    # fastest:
    print(turnsF, turnsL)
    return int(min(turnsL, turnsF))

print(int(pageCount(6, 2)))
