def matrix_transpose(X): 
    m = [[0 for _ in range(len(X))] for _ in range(len(X[0]))]
    for i in range(len(X[0])):
        for j in range((len(X))):
            m[i][j] = X[j][i]
    return m

X = [[1, 2, 3],    
     [4, 5, 6]] 
answer = matrix_transpose(X)
print(answer)