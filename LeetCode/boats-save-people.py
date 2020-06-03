def boats-save-people(weights, limit=None):
    if limit < max(weights): limit = max(weights)
    if len(weights) <= 1: return len(weights)
    weights.sort()
    boat_count = 0
    i, j = 0, len(weights)-1
    while i <= j:
        if weights[i] + weights[j] > limit:
            boat_count += 1
            j -= 1
        else:
            boat_count += 1
            i, j = i + 1, j - 1
    return boat_count
