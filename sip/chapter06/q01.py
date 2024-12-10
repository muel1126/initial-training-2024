def vector_sum(x,y):
    v=[]
    for i, j in zip(x,y):
        v.append(i+j) 
    return v

x = [1,2,3]
y = [8,1,2]
answer = vector_sum(x, y)
print(answer)