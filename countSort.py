def countSort(arr):
    # replace string with dashes
    
    for i in range(len(arr)):
        
        if i < len(arr)/2:
            arr[i][1] = "-"
        
    
    # sort
    count = [[''*i] for i in range(len(arr))]
    for elem in arr:
        count[int(elem[0])].append(elem[1])
    x = ""
    del count[0][0]
    
    print(*[' '.join(m) for m in count], sep="")
        
        

countSort([['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], 
['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], ['0', 'to'],
['1', 'be'], ['5', 'question'], ['1', 'or'], ['2', 'not'], ['4', 'is'], ['2', 'to'], ['4', 'the']])
