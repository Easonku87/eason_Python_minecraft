A = [10,25,31,2,4,6,99,-1,34]
for i in range(3):
    for j in range(3):
        if A[i] > A[j]:
            print(i,A[i],j,A[j])
            t = A[i]
            A[i] = A[j]
            A[j] = t
print(A)
            
            