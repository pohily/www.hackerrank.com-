def climbingLeaderboard(scores, alice):
  results = []

  # 1 make list of lists of results
  unic_scores = set(scores)
  chart = [[0*x] for x in range(len(unic_scores))]
  chart_index = 0
  chart[chart_index].append(scores[0])
  
  for s in range(1, len(scores)):
    if scores[s] == scores[s-1]:
      chart[chart_index].append(scores[s])
    else:
      chart_index += 1
      chart[chart_index].append(scores[s])
      

  # 2 make result list for Alice's scores
  for a in alice:
    if a < min(scores):
      results.append(len(chart) + 1)
      print(len(chart) + 1, end = " ")
    for c in range(len(chart)):
      if a >= chart[c][-1]:
        results.append(c+1)
        print(c+1, end = " ")
        break
      
  
  return results

      






#climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 120])




  
