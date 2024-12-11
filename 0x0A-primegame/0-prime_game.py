#!/usr/bin/python3
"""Maria and Ben are playing Prime game"""


def sieve_of_eratosthenes(n):
    """
    use to generate prime numbers up to n limit
    :param n:
    :return:
    """
    # Initialize a list to track prime number(assume all are prime)
    prime = [True for i in range(n + 1)]
    p = 2

    # Sieve algorithm: Mark non-prime numbers
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):  # Mark multip p non prime
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            print(p)


def isWinner(numRounds, roundValues):
    if not numRounds or not roundValues:
        return None
    mariaScore = benScore = 0
    for i in range(numRounds):
        primes = sieve_of_eratosthenes(roundValues[i])
        if len(primes) % 2 == 0:
            benScore += 1
        else:
            mariaScore += 1
    if mariaScore > benScore:
        return "Maria"
    elif benScore > mariaScore:
        return "Ben"
    return None
