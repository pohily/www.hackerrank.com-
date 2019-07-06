def marcsCakewalk(calorie):
    calorie = sorted(calorie, reverse=True)
    return sum([pow(2, i) * calorie[i] for i in range(len(calorie))])
