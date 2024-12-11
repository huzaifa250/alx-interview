#!/usr/bin/python3
"""Maria and Ben are playing Prime game"""


def sieve_of_eratosthenes(n):
    """
    use to generate prime numbers up to n limit
    :param n:
    :return:
    """
    primeNumbers = []
    # Initialize a list (assume all are prime)
    prime = [True for i in range(n + 1)]
    for potentialPrime in range(2, n + 1):
        if prime[potentialPrime]:
            primeNumbers.append(potentialPrime)
            for multiple in range(potentialPrime, n + 1, potentialPrime):
                sieveList[multiple] = False
    return primeNumbers


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
