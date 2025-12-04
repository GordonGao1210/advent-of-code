def find_factors(number: int) -> list[int]:
    """
    Find all factors of a given number except 1 and the number itself.
    Returns a sorted list of factors.
    """
    factors = []
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    factors = sorted(set(factors))
    return factors


def find_prime_factors(number: int) -> list[int]:
    """
    Find all prime factors of a given number.
    Returns a sorted list of prime factors.
    """
    factors = find_factors(number)
    prime_factors = [f for f in factors if is_prime(f)]
    return prime_factors


def is_prime(n: int) -> bool:
    """
    Determine if a number is prime. 1 is not considered prime, and 2 is the only even prime.
    """
    if n <= 1:
        return False
    factors = find_factors(n)
    if len(factors) > 0:
        return False
    return True
