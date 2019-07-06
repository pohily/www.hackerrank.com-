def queensAttack(n, k, r_q, c_q, obstacles):
    result = 0
                                            ###  c = hor, r = ver
                                            ###  up
    if r_q < n:
        for ver in range(n - r_q):
            if [r_q + ver + 1, c_q] not in obstacles:  
               result +=1
            else:
                break
        print("up ", result)
                                            ###  down
    if r_q > 1:
        for ver in range(r_q - 1):
            if [r_q - ver - 1, c_q] not in obstacles:  
                result +=1
            else:
                break
        print("down ", result)
                                            ###  left
    if c_q > 1:
        for hor in range(c_q - 1):
            if [r_q, c_q - hor - 1] not in obstacles:  
                result +=1
            else:
                break
        print("left ", result)
                                            ###  right
    if c_q < n:
        for hor in range(n - c_q):
            if [r_q, c_q + hor + 1] not in obstacles:  
                result +=1
            else:
                break
        print("right ", result)
                                            ###  up  rigth
    if r_q < n and c_q < n:
        for diag in range(min((n - r_q), (n - c_q))):
            if [r_q + diag + 1, c_q + diag + 1] not in obstacles:  
                result +=1
            else:
                break
        print("up right ", result)
                                            ###  down right
    if r_q > 1 and c_q < n:
        for diag in range(min((r_q - 1), (n - c_q))):
            if [r_q - diag - 1, c_q + diag + 1] not in obstacles:  
                result +=1
            else:
                break
        print("down right ", result)
                                            ###  down left
    if r_q > 1 and c_q > 1:
        for diag in range(min((r_q - 1), (c_q - 1))):
            if [r_q - diag - 1, c_q - diag - 1] not in obstacles:  
                result +=1
            else:
                break
        print("down left ", result)
                                            ###  up left
    if r_q < n and c_q > 1:
        for diag in range(min((n - r_q), (c_q - 1))):
            if [r_q + diag + 1, c_q - diag - 1] not in obstacles:  
                result +=1
            else:
                break
        print("up left ", result)
    return result

print(queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))
#print(queensAttack(8, 1, 4, 4, [3, 5]))
#print(queensAttack(8, 0, 4, 4, []))


