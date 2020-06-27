def numJewelsInStones(J, S):
    count = 0
    J = set(J)
    for stone in S:
        if stone in J:
            count += 1
    return count
