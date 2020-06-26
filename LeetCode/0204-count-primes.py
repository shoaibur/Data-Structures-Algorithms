def count_primes(n):
    count = 0
    primes = [True] * n
    for i in range(2, n):
        if primes[i]:
            for j in range(i, n, i):
                primes[j] = False
            count += 1
    return count
