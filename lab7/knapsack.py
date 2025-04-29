def knapsack(values: list, weights: list, capacity: list) -> int:
    # Liczba przedmiotów
    n = len(values)

    # Tworzenie tablict DP z zerami

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Wypłnianie tablicy DP

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # Maksymalna wartość, która może być przeniesiona w plecaku
    return dp[n][capacity]

print(knapsack([60,100,120], [10, 20, 30], 50))