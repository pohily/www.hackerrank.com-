def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    print(scores)
    print(alice)
    
    results = []
    for game in alice:
        if game in scores:
            results.append(len(scores) - scores.index(game))
        else:
            scores.append(game)
            scores = sorted(scores)
            results.append(len(scores) - scores.index(game))
    return results

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))


