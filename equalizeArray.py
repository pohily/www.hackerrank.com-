def equalizeArray(arr):
  new = list(set(arr))
  count_number = [arr.count(i) for i in new]
  if max(count_number) > 1:
    return len(arr) - max(count_number)
  else:
    return len(arr) - 1

print(equalizeArray([3, 3, 2, 1, 3]))