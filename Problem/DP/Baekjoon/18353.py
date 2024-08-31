def main(N, SOLDIER):
    dp = [0] * (N + 1)
    SOLDIER = [0] + SOLDIER

    dp[1] = 1  # 1번

    for i in range(2, N + 1):  # 2 ~ N번
        temp_dp_table = []
        for j in range(1, i):  # 1 ~ (i - 1)번
            if SOLDIER[j] > SOLDIER[i]:
                temp_dp_table.append(dp[j])
        if temp_dp_table:
            dp[i] = max(temp_dp_table) + 1
        else:
            dp[i] = 1  # 이전에 더 큰 게 없으면 이어질 게 없으므로 1
    print(N - max(dp))  # 마지막 수가 가장 큰 수라면 dp[-1]은 틀림
    return


def best(N, SOLDIER):
    dp = [1] * (N + 1)  # 자기 자신만 있어도 값은 1이므로
    SOLDIER = [0] + SOLDIER

    for i in range(2, N + 1):  # 2 ~ N번
        for j in range(1, i):  # 1 ~ (i - 1)번
            if SOLDIER[j] > SOLDIER[i]:
                # temp list 설정 안 해도 가능
                dp[i] = max(dp[i], dp[j] + 1)
    print(N - max(dp))
    return


if __name__ == "__main__":
    N = int(input())
    SOLDIER = list(map(int, input().split()))
    best(N, SOLDIER)
