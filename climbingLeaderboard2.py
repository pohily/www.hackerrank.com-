def climbingLeaderboard(scores, alice):
    results = []
    scores = list(sorted(set(scores)))
    print(scores)
    print(alice)
    start = 0
    l = len(scores)
    for game in alice:
        ins = False
        for index, score in enumerate(scores[start:]):
            if game < score:
                results.append(l-start - index + 1)
                
                start += index + 1
                print(start)
                ins = True
                break
            elif game == score:
                results.append(l-start - index)
                
                start += index + 1
                print(start)
                ins = True
                
                break
        if ins == False:
            results.append(1)
       
    return results

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
#climbingLeaderboard(a, b)

