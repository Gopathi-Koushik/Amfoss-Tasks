def count_ways(X, N):
    # dp[i] will store the number of ways to express i as the sum of distinct powers
    dp = [0] * (X + 1)
    dp[0] = 1  
    
    i = 1
    while i ** N <= X:
        power = i ** N
        for j in range(X, power - 1, -1):
            dp[j] += dp[j - power]
        i += 1

    return dp[X]

X = int(raw_input()) 
N = int(raw_input())  # Power


print(count_ways(X, N))

