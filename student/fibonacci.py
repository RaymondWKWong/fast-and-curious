from numba import jit

@jit(nopython=True)
def fib_doubling(n):
    if n == 0:
        return 0, 1
    k = n // 2
    fk, fkp1 = fib_doubling(k)
    fk2 = fk * fk
    fkp12 = fkp1 * fkp1
    f2k = fk * (2 * fkp1 - fk)
    f2kp1 = fkp12 + fk2
    if n % 2 == 0:
        return f2k, f2kp1
    else:
        return f2kp1, f2k + f2kp1
        
@jit(nopython=True)
def fibonacci(n):
    if n == 0:
        return 0
    return fib_doubling(n)[0]