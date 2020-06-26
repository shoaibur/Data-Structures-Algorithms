def get_row(n):
    if n == 0: return [1]
    out = [1, 1]
    for k in range(2, n+1):
        out = [1]+[out[i]+out[i+1] for i in range(len(out)-1)]+[1]
    return out

    ''' solution 2
    if n == 0: return [1]
    a = [1, 1]
    for i in range(2, n+1):
        for j in range(len(a)-1):
            a[j] = a[j] + a[j+1]
        a = [1] + a
    return a
    '''
