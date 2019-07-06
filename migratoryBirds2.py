def migratoryBirds(arr):
    viewed = [0]*6
    for bird in arr:
        viewed[bird] += 1
    
    return viewed.index(max(viewed))

print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4, 4]))
