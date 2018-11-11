def bonAppetit(bill, k, b):
  change = (sum(bill) - bill[k])/2
  if change == b:
    return "Bon Appetit"
  else:
    return int(b - change)

print(bonAppetit([3, 10, 2, 9], 1, 12))
