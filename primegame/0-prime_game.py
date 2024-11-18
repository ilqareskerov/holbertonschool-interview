
#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game
    """

    # Vérifier que le nombre de rounds est correct
    if x != len(nums):
        return None

    # Trier la liste nums
    nums.sort()

    # Générer tous les nombres premiers jusqu'au maximum de nums
    primes = sieve_of_eratosthenes(max(nums))

    # Initialiser les compteurs de victoires pour Maria et Ben
    maria_wins = 0
    ben_wins = 0

    # Boucle sur chaque round
    for n in nums:
        prime_count = 0
        for prime in primes:
            if prime <= n:
                prime_count += 1
            else:
                break

        # Si le nombre de nombres premiers est impair, Maria gagne ce round
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Déterminer le gagnant global
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(n):
    """Générer tous les nombres premiers jusqu'à n"""
    primes = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]
