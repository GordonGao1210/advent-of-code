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


def calculate_euclidean_distance(
    position_1: tuple[int, ...] | list[int], position_2: tuple[int, ...] | list[int]
) -> float:
    """
    Calculate the Euclidean distance between two points in n-dimensional space.
    """
    if len(position_1) != len(position_2):
        raise ValueError("Positions must have the same number of dimensions.")
    distance = (
        sum((position_1[i] - position_2[i]) ** 2 for i in range(len(position_1))) ** 0.5
    )
    return distance
