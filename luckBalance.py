def luckBalance(k, contests):
    # find quantity of important contests
    importantList = [contests[i][0] for i in range(len(contests)) if contests[i][1] == 1]
    important = len(importantList)

    # if thare are number of imp. cont. to win - find number of min lucks
    if k >= important:
        return sum([contests[i][0] for i in range(len(contests))])
    
    else:
        toWin = []
        for i in range(important - k):
            toWin.append(min(importantList))
            importantList.remove(min(importantList))
            
    
    # count luck
    return sum(importantList) + sum(contests[i][0] for i in range(len(contests)) if contests[i][1] == 0)  - sum(toWin)



print(luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))

