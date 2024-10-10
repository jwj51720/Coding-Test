def main(T, NUMS):
    """
    1이라는 숫자가 T까지 도달하기 위한 방식의 총 개수로 생각
    - i는 숫자 자체, a_i는 도달하는 방법의 총 개수
    - +1, +2, +3이라는 선택지가 있으므로, a_i = a_{i-1} + a_{i-2} + a_{i-3}
    0 -> 0
    1 -> 1
    2 -> 2
    3 -> 4
    4 -> 7 ...
    """
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for num in NUMS:
        for i in range(4, 11):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        print(dp[num])
    return


if __name__ == "__main__":
    T = int(input())
    NUMS = [int(input()) for _ in range(T)]
    main(T, NUMS)
