def calculate_team_score(team, S):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            score += S[team[i]][team[j]] + S[team[j]][team[i]]
    return score

def backtracking(idx, N, S, start_team, min_diff):
    if 1 <= len(start_team) <= N - 1:
        link_team = [i for i in range(N) if i not in start_team]  # 링크 팀은 나머지 사람들로 구성
        start_score = calculate_team_score(start_team, S)
        link_score = calculate_team_score(link_team, S)
        diff = abs(start_score - link_score)
        min_diff[0] = min(min_diff[0], diff)
        if start_score >= link_score:
            return
        
    for i in range(idx, N):
        start_team.append(i)
        backtracking(i + 1, N, S, start_team, min_diff)
        start_team.pop()
        

def main(N, S):
    """
    min_diff가 구하려는 값이며, backtracking을 하며 값을 저장하기 위해 list를 사용
    start_team뿐만 아니라 여러 값을 backtracking에서 가지고 다닐 수 있는데,
    시간복잡도에 큰 영향을 주지 않는 요소라면 굳이 가지고 다니지 말고,
    최소한의 것만 가지고 다니자. 그 최소한의 것이 min_diff(정답), start_team
    ** python3는 시간초과가 나고, pypy3로 하면 시간초과가 안 난다.
    ** N-1, N//2 모두 정답이긴 하나, N-1이 더 적은 횟수로 돈다.
    ** if start_score >= link_score: 탈출을 하지 않아도 가능하다.
    """
    min_diff = [float('inf')]
    backtracking(0, N, S, [], min_diff)
    print(min_diff[0])
    return


if __name__ == "__main__":
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    main(N, S)
