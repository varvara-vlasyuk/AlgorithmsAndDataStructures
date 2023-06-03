"""
Given coins of different denominations and total amount of money. Find the minimum number of coins
that you need to make up the given amount. You can use each denomination multiple times.
"""

denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
total = 3
nom = []
i = len(denominations) - 1
while total > 0 and i >= 0:
    if denominations[i] <= total:
        total = total - denominations[i]
        nom.append(denominations[i])
    else:
        i -= 1

print(nom)
