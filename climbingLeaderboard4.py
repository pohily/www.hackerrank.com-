def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    
    
    l = len(scores)
    print(l)
    results = []
    for game in alice:
        
        if game > max(scores):
            results.append(1)
            scores.append(game)
            l += 1
            continue
        for index, score in enumerate(scores):
            if game < score:
                results.append(l - index + 1)
                l += 1
                scores = scores[:index] + [game] + scores[index:]
                break
            elif game == score:
                results.append(l - index)
                break

    return results

print(climbingLeaderboard(

