def matrix_vector_product(X, y):
    m=[]
    for i in X:
        s=0
        for j in range(len(X[0])):
            s += (i[j]*y[j])
        m.append(s)
    return m

X = [[1, 2, 3],    
     [4, 5, 6]] 
y = [8, 1, 2] 
answer = matrix_vector_product(X, y) 
print(answer)