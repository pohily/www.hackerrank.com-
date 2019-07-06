def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    l = len(scores)
    m = max(scores)
    i = 0
    results = []
    for game in alice:
        if game > m:
            results.append(1)
            scores.append(game)
            l += 1
            continue
        for index, score in enumerate(scores):
            if game < score:
                results.append(l - index + 1 - i)
                l += 1
                scores = [game] + scores[index:]
                i += index 
                break
            elif game == score:
                results.append(l - index - i)
                scores = scores[index:]
                i += index
                break

    return results

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))


