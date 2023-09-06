#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of a prime game played x rounds.

    Args:
        x (int): The number of rounds.
        nums (List[int]): An array of n values representing the maximum
        integer for each round.

    Returns:
        str: The name of the player that won the most rounds, or None if
        the winner cannot be determined.
    """
    def is_prime(n):
        """
        Checks if a given number is prime.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if n is prime, False otherwise.
        """
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        """
        Returns a list of all prime numbers up to and including a given
        maximum value.

        Args:
            n (int): The maximum value.

        Returns:
            List[int]: A list of prime numbers up to and including n.
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_game(n):
        """
        Simulates a single round of the game and returns the name of the
        winner.

        Args:
            n (int): The maximum integer for the round.

        Returns:
            str: The name of the winner.
        """
        primes = get_primes(n)
        turn = 0
        while primes:
            for prime in primes:
                multiples = [prime * i for i in range(1, n // prime + 1)]
                primes = [x for x in primes if x not in multiples]
                turn += 1
                break
        if turn % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    results = []
    for n in nums:
        results.append(play_game(n))
    maria_wins = results.count("Maria")
    ben_wins = results.count("Ben")
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
