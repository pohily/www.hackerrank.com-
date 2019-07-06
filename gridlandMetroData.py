track = []
with open('data1', 'r') as k:
    for i in k:
        track.append(list(map(int, i.rstrip().split())))
print(sorted(track))
