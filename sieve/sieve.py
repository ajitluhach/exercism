def sieve(limit, start=2):
    primes = []
    multiples = [True]*limit
    multiples.append(True)
    for num in range(start, limit+1):
        if multiples[num] is True:
            primes.append(num)
            j = 2
            while j*num <= limit:
                multiples[j*num] = False
                j += 1
    return primes
