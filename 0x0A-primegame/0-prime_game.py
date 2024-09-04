#!/usr/bin/python3


def is_prime(n):
    """Check if n is a prime number."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def isWinner(x, nums):
    """Return the name of the player that won the most rounds."""
    Maria = 0
    Ben = 0

    for n in nums:
        if n == 1:
            Ben += 1
            continue

        primes = [i for i in range(2, n + 1) if is_prime(i)]
        turn = 0

        while primes:
            current_prime = primes.pop(0)
            primes = [p for p in primes if p % current_prime != 0]
            turn += 1

        if turn % 2 != 0:
            Maria += 1
        else:
            Ben += 1

    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
