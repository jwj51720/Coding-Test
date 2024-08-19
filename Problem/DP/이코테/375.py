# fmt:off
def main(N, M, matrix):
    dp = [[0] * (M + 1) for _ in range(N)] # dp를 3개 동시에
    for row in range(N):
        dp[row][1] = matrix[row][0]

    for i in range(2, M + 1):
        for row in range(N):
            if row == 0:
                dp[row][i] = max(dp[row][i - 1], dp[row + 1][i - 1]) + matrix[row][i - 1]
            elif row == 1:
                dp[row][i] = max(dp[row][i - 1], dp[row + 1][i - 1], dp[row - 1][i - 1])+ matrix[row][i - 1]
            else:
                dp[row][i] = max(dp[row][i - 1], dp[row - 1][i - 1]) + matrix[row][i - 1]
    print(max([dp[r][M] for r in range(N)]))
    return
# fmt:on

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        matrix = [[] for _ in range(N)]
        array = list(map(int, input().split()))
        for i in range(N):
            matrix[i] = array[i * M : i * M + M]
        main(N, M, matrix)
