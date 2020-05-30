def jewels_and_stones(J, S):
    count = 0
    for stones in S:
        if stones in J:
            count += 1
    return count
    
