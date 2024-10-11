def is_valid(sum_sol, N, i):
    if sum_sol + i <= N:
        return True
    return False


def backtracking(solution, sum_sol, N, K, results):
    if len(solution) == K and sum_sol == N:
        results.append(solution[:])
        return
    
    for i in range(N + 1):
        if is_valid(sum_sol, N, i) and len(solution) < K:
            solution.append(i)
            sum_sol += i
            backtracking(solution, sum_sol, N, K, results)
            sum_sol -= i
            solution.pop()

def main_backtracking(N, K):
    """
    한 개를 선택하고, 그 다음 것을 선택하고, ... 경우의 수가 많고, 선택을 되돌릴 수 있으면 좋겠어서 Backtracking
    테스트 케이스는 맞았어도 시간초과가 발생 -> 탐색하지 않아도 될 부분을 탐색/어딘가에서 중복 탐색
    탐색하지 않아도 될 부분은 생각해봐도 없음, 어딘가에서 중복해서 탐색하고 있기 때문으로 추정
    생각해보면, 어떤 숫자를 만드는 경우의 수만 관심이 있는 것 -> 4를 만들 때에 2를 만드는 경우의 수를 그대로 사용 가능
    4를 만들 때에, 1 + 1 + 2, 1 + 2 + 1, 2 + 1 + 1, 1 + 1 + 1 + 1, ...을 서로 다른 경로로 다 구할 필요 없음
    4는 4개 숫자로 표할 때, 3개 숫자로 표현할 때, ... 각 경우에 몇 가지인지만 알면 됨
    DP를 떠올릴 수 있음(사실 숫자를 더해서 어떤 숫자가 되는 경우의 수를 묻는 문제는 전형적인 DP 형태)
    """
    results = []
    backtracking([], 0, N, K, results)
    print(len(results)%1000000000)
    return

def main_dp(N, K):
    """
    N = 1 때, K = 1이면 1, K = 2이면 2, K = 3이면 3, ...
    N = 2 때, K = 1이면 1, K = 2이면 3, K = 3이면 6, ...
    N = 3 때, K = 1이면 1, K = 2이면 4, K = 3이면 10, ...
    N = 4 때, K = 1이면 1, K = 2이면 5, K = 3이면 15?, ...
    2차원 배열로 DP를 사용할 수 있음
    i, j를 N과 K의 값이라고 하고, a_{ij}를 해당 경우의 표현 가지 수라고 하면,
    i - 1일 때의 값에서 +1밖에 선택지가 없으며, j - 1의 경우에서 0을 채워 넣는 선택지만 있음
    a[i][j] = a[i][j - 1] + a[i - 1][j] 
    """
    dp = [[i + 1 for i in range(K)] for _ in range(N)]
    
    for i in range(1, N):
        for j in range(1, K):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
    print(dp[N - 1][K - 1]%1000000000)
    return

if __name__ == "__main__":
    N, K = map(int, input().split())
    main_dp(N, K)
