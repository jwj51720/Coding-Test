def main(N, T, P):
    """
    하나를 선택하면, 그 다음 것을 선택 못 할 수도 있는 상황에서 값을 최대화하는 전형적인 DP
    날짜가 i, 그 날짜에 가장 많이 버는 돈이 a_i
    
    하지만, 돈을 받는 것은 N일 안에 해당 상담을 온전히 마친 경우임
    따라서 dp 업데이트는 i일이라도 i + T[i] 후에 하는 게 맞음
    * 기존 DP는 dp[i]만 채웠었는데, 여기서는 미래 칸을 먼저 채우는 시도를 함
    상담이 끝나는 날(돈을 받는 날)에 가장 큰 값은 무엇인지?
    만약 어떤 날짜에 상담이 끝나는 경우가 없으면 0이 계속 기록되어 있으므로
    dp[i] = max(dp[i], dp[i - 1]) 이전 날의 최댓값을 불러옴
    
    아니면, 끝나는 날에 돈을 받는다는 것(dp가 갱신된다는 것)을 힌트로, 뒤에서부터 DP도 가능
    이러면 기존 DP에서 접근하는 대로 dp[i]만 채우는 방식이 가능함
    이 방식이 조금 더 정형화되어 있는 풀이 가능
    """
    dp = [0] * (N + 1)
    
    for i in range(1, N + 1):
        if i + T[i] - 1 <= N:
            dp[i + T[i] - 1] = max(dp[i + T[i] - 1], dp[i - 1] + P[i])
        dp[i] = max(dp[i], dp[i - 1])

    print(max(dp))


if __name__ == "__main__":
    N = int(input())
    T, P = [0], [0]
    for t, p in [list(map(int, input().split())) for _ in range(N)]:
        T.append(t)
        P.append(p)
    main(N, T, P)
