def knapsack_donut(values, weights, capacity, names):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    w = capacity
    selected = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]

    print("Wybrane pączki: ")
    counts = {}
    for p in selected:
        counts[names[p]] = counts.get(names[p], 0) + 1

    for name,count in counts.items():
        print(f"  {count} x {name}")

    return dp[n][capacity]

names = ["pączek wiśniowy", "fit pączek gryczany ze śliwkami", "pączek z czekoladą", "pączek karmelowo-orzechowy", "oreo donut", "mini pączek z budyniem"]
values = [252, 205, 315, 441, 630, 126]
weights = [100, 200, 150, 100, 150, 50]
capacity = 500

max_value = knapsack_donut(values, weights, capacity, names)
print(f"Maksymalna ilość kalorii: {max_value}")