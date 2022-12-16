from random import randrange

# for a,b > 0 returns x, y, gcd(a,b) such that ax + by = gcd(a,b)
def extended_euclidean_algorithm(a: int, b: int):
    return recursive_extended_euclidean_algorithm(a, b, [1, 0], [0, 1])

# recursive function to find gcd as well as Bézout’s coefficients - according to table in tutorial
def recursive_extended_euclidean_algorithm(a: int, b: int, s: list, t: list):
    if a % b == 0:
        return s[1], t[1], b
    else:
        return recursive_extended_euclidean_algorithm(b, 
                                                      a % b, 
                                                      [s[1], s[0] - (a // b)*s[1]], 
                                                      [t[1], t[0] - (a // b)*t[1]])

def extended_gcd(a,b):
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """
    x, y, gcd = extended_euclidean_algorithm(a, b)
    return gcd, x, y

def modular_inverse(a,n):
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    gcd, x, y = extended_gcd(a, n)
    if gcd == 1:
        return x % n
    else: 
        return None


def modular_exponent(a, d, n):
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    """
    acc = 1
    partial_exponent = a
    while d > 0:
        if d % 2 == 1:
            acc = acc * partial_exponent % n
        partial_exponent = (partial_exponent * partial_exponent) % n
        d //= 2
    return acc

def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1,n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False

def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True

def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None