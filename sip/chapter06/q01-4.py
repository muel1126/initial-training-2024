def matrix_product(X, Y):  
    m=[[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(X[0])):
                m[i][j] += X[i][k]*Y[k][j]  
  
        
    return m
    
    
X = [[1, 2, 3],    
     [4, 5, 6]] 
Y = [[8, 1],    
     [-1, 0],    
     [0, 1]] 
answer = matrix_product(X, Y) 
print(answer)