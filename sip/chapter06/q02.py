def matrix_sum(X,Y):
    m=[[0 for _ in range(len(X[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            m[i][j] = X[i][j] + Y[i][j]
    return m

X = [[1, 2, 3],
    [4, 5, 6]]
Y = [[8, 1, 2],
    [-1, 0, -2]]
answer = matrix_sum(X, Y)
print(answer)