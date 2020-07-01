def arrangeCoins(n)
    a = int(-1/2 + math.sqrt( 1 + 8 * n ) / 2)
    b = int(-1/2 - math.sqrt( 1 + 8 * n ) / 2)
    return max(a, b)
    # k(k+1)/2 <= n
    # k2 + k - 2n <= 0
