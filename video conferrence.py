def solve(names):
  prefs = []

  for index in range(len(names)):
# проверяем от одной буквы до всего имени, если нет совпадений - добавляем
  


    for i in range(1, len(names[index])+1):

      if names[index][:i] not in prefs:
        prefs.append(names[index][:i])
        names.pop(index)
        break


# если все имя входит, ищем первый суффикс с которым не входит и добавляем
    if names[index] in prefs:

      for suffix in range(1, len(names)-1):

        if (names[index] + str(suffix)) not in prefs:
          prefs.append(names[index] + str(suffix))
          names.pop(index)
          break

  return prefs

names = ["mary", "stacy", "sam", "samuel", "sam", "samuel"]
print(solve(names))

    
