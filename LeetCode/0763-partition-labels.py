def partitionLabels(S):
    out = []
    last_indices = { char:i for i, char in enumerate(S) }
    start = 0
    end = 0
    for i, char in enumerate(S):
        end = max(end, last_indices[char])
        if i == end:
            out.append(end-start+1)
            start = end + 1
    return out
