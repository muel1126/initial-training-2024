import numpy as np

A = np.array([[2,-1],[1,1]])
x = np.array([1,1])
b = np.array([1,2])

Ax = np.matmul(A,x)
ans = np.subtract(Ax,b)
print(ans)