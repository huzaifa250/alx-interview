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


def playGame(n):
    """
    Simulate one round of the game for a given number n.
    Returns the winner of the round: "Maria" or "Ben".
    """
    primes = sieve_of_eratosthenes(n)
    availableNumbers = set(range(2, n + 1))  # Numbers available to pick
    turn = 0  # 0 for Maria, 1 for Ben (alternate turns)

    while primes:
        moveMade = False
        for prime in primes:
            if prime in availableNumbers:
                # Remove the prime and its multiples from the available nums
                for multiple in range(prime, n + 1, prime):
                    availableNumbers.discard(multiple)
                moveMade = True
                break  # Move to the next turn after a move is made

        if not moveMade:
            break  # If no valid moves are possible, the game ends

        # Switch turns
        turn = 1 - turn

    # If the game ends, the player who cannot make a move loses
    return "Maria" if turn == 1 else "Ben"


def isWinner(numRounds, roundValues):
    """
    Determine the overall winner of the game.
    """
    if not numRounds or not roundValues:
        return None

    mariaScore = benScore = 0

    for i in range(numRounds):
        winner = playGame(roundValues[i])
        if winner == "Maria":
            mariaScore += 1
        elif winner == "Ben":
            benScore += 1

    if mariaScore > benScore:
        return "Maria"
    elif benScore > mariaScore:
        return "Ben"
    return None
