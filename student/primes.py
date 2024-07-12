import numpy as np
from numba import jit

@jit(nopython=True)
def sieve_of_eratosthenes(n):

    is_prime = np.ones(n+1, dtype=np.bool_)
    is_prime[:2] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i:n+1:i] = False  # Mark all multiples of i as not prime

    primes = np.nonzero(is_prime)[0]
    return primes

def write_primes(n, path):
    primes = sieve_of_eratosthenes(n)

    # Write the prime numbers to the file
    with open(path, 'w') as file:
        file.write('\n'.join(map(str, primes)))

# Example usage

write_primes(100, 'primes.txt')
