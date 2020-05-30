def merge_sorted_arrays(a1, a2):
    a = []
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            a.append(a1[i])
            i += 1
        else:
            a.append(a2[j])
            j += 1
    a += a1[i:]
    a += a2[j:]
    return a
