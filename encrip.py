import math


def encryption(s):
    matrix = []
    bufer = []
    
    matrix_lenth = math.ceil((math.sqrt(len(s))))
    if math.ceil((math.sqrt(len(s)))) * math.floor((math.sqrt(len(s)))) > len(s):
        delta = math.ceil((math.sqrt(len(s)))) * math.floor((math.sqrt(len(s)))) - len(s)
    else:
        delta = math.ceil((math.sqrt(len(s))))**2 - len(s)
    #print(delta)
    #print(matrix_lenth)
     
    s += (" "*delta)
    #print(s)
    #print(len(s))
   
    
    for i in range(matrix_lenth):
        bufer = s[:(matrix_lenth)]
        #print(bufer)
        matrix.append(bufer)
        s = s[(matrix_lenth):]
        
        
    #print(matrix)   
    
             
    matrix_trans = list(zip(*matrix))
    result = ""
    for i in range(len(matrix_trans)):
        for j in range(len(matrix_trans[i])):
            result += matrix_trans[i][j]
        if result[-1] != " ":
            result = result + " "
    print(result)       
    while result[-1] == " ":
        result = result[:-1]
    return result
        


print(encryption("feedthedog"))

#encryption("have a nice day")
