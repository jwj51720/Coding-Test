def main(N, M, PRICE):
    """
    i: 금액 그 자체
    a_i = 그 금액을 구성하는 최적의 동전 개수
    i를 돌면서 동시에 p를 체크
    """
    dp = [0] * 10001
    for p in PRICE:
        dp[p] = 1

    for i in range(1, M + 1):
        temp = [0] * N
        for idx, p in enumerate(PRICE):
            if i - p > 0:
                temp[idx] = dp[i - p]
        temp = [t for t in temp if t != 0]
        dp[i] = min([t for t in temp if t != 0]) + 1 if temp else dp[i]
    answer = dp[M] if dp[M] else -1
    print(answer)
    return 0


def answer(N, M, PRICE):
    """
    i: 금액 그 자체
    a_i = 그 금액을 구성하는 최적의 동전 개수
    p가 각각 i를 돌기
    """
    dp = [float("inf")] * (M + 1)  # dp를 inf로 초기화
    dp[0] = 0

    for p in PRICE:  # PRICE 하나씩
        for i in range(p, M + 1):  # 금액 그 자체 i에 대해 돌기
            if dp[i - p] != float("inf"):
                dp[i] = min(dp[i], dp[i - p] + 1)
    answer = dp[M] if dp[M] != float("inf") else -1
    print(answer)
    return 0


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    PRICE = [int(input()) for _ in range(N)]
    main(N, M, PRICE)
