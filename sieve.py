def sieve_primes(n):
    primes = {2: True}

    for i in range(2, n+1):
        if primes.get(i) == False:
            continue
        else:
            primes[i] = True

            for j in range(i+i, n+1, i):
               primes[j] = False 
