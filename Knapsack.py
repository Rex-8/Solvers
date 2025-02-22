def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


weights = []    ## The weights of each element
values = []     ## the values of each element
capacity = 0    ## The capacity that the man can carry

max_value = knapsack(weights, values, capacity)
print(f"The maximum value in the knapsack is: {max_value}")
