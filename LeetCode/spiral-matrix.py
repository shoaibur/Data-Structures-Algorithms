def spiral_matrix(matrix):
    if not matrix: return matrix
    out = []
    while True:
        if matrix != []:
            out += matrix.pop(0)
        if matrix != []:
            for i in range(len(matrix)):
                out.append(matrix[i].pop())
        if matrix != []:
            out += matrix.pop()[::-1]
        if matrix != []:
            for i in range(len(matrix)-1,-1,-1):
                out.append(matrix[i].pop(0))
        if matrix == []:
            break
    return out
