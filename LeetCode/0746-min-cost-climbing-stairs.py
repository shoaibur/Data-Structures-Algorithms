def minCostClimbingStairs(cost):
    c1, c2 = 0, 0
    for c in cost:
        c1, c2 = c2, c + min(c1, c2)
    return min(c1, c2)
