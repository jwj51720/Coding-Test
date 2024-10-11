import math

def main(N):
    """
    제곱수를 한 번 써 본다.
    1 -> 1, 2 -> 4, 3 -> 9, 4 -> 16, 5 -> 25, ...
    최소한의 개수니까, 그리디로 선택하면? 테스트 케이스에 대해서는 모두 OK
    
    하지만 틀림 -> N = 12라면, 9 + 1 + 1 + 1 > 4 + 4 + 4
    숫자를 조합해서 어떤 수를 만드는 형태는 DP에서 익숙함 -> DP로 접근
    i가 숫자 자체이고, a_i가 그 숫자를 구성할 수 있는 최소 경우의 수라면,
    i로부터 제곱수를 뺀 모든 경우에 대해 a_{i-j**2} + 1의 최솟값을 취하면 됨
    """
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            # j를 돌면서 dp 같은 index 값을 계속 갱신해
            # 후보군 list를 만들지 않아도 후보군 중 min을 찾을 수 있음
            dp[i] = min(dp[i], dp[i - j ** 2] + 1)

    print(dp[N])

if __name__ == "__main__":
    N = int(input())
    main(N)