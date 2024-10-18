def main(N, A):
    dp = [1] * N
    trace = [-1] * N
    
    for i in range(1, N):
        for j in range(0, i):
            if A[j] < A[i]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    trace[i] = j

    print(max(dp))
    before = trace[dp.index(max(dp))]
    result = [A[dp.index(max(dp))]]
    while before >= 0:
        result.append(A[before])
        before = trace[before]
    result.reverse()
    print(*result, sep=" ")


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    main(N, A)
