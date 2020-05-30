def flipping_image(A): # Vertical flip
    if not A: return A
    i, j = 0, len(A)-1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i, j = i+1, j-1
    nrow = len(A)
    ncol = len(A[0])
    for i in range(nrow):
        for j in range(ncol):
            if A[i][j] == 1:
                A[i][j] = 0
            else:
                A[i][j] = 1
    return A

def flipping_image(A): # Horizontal flip  
    A = transpose(A)
    i, j = 0, len(A)-1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i, j = i+1, j-1
    nrow = len(A)
    ncol = len(A[0])
    for i in range(nrow):
        for j in range(ncol):
            A[i][j] = 1 - A[i][j] # Flip between 0 and 1.
    return transpose(A)

def transpose(A):
    A = [*zip(*A)]
    # A = [list(A[i]) for i in range(len(A))]
    A = [ list(row) for row in A ]
    return A
    
