def main(N):
    dp = [0] * (10**6 + 1)
    dp[N] = 0
    for i in range(N-1,0,-1):
        if i * 3 <= N:
            dp[i] = min(dp[i+1], dp[i*2], dp[i*3]) + 1
        elif i * 2 <= N:
            dp[i] = min(dp[i+1], dp[i*2]) + 1
        else:
            dp[i] = dp[i+1] + 1
    print(dp[1])
    return 0
            

if __name__ == "__main__":
    N = int(input())
    main(N)