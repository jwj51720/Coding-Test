def is_valid(solution, v):
    """solution에 담긴 노드와 인접하지 않으면 후보군 True"""
    row, col = v[0], v[1]
    for dx, dy in zip([-1, 1, 0, 0], [0, 0, 1, -1]):
        if [row + dx, col + dy] in solution or v in solution:
            return False
    return True


def backtracking(solution, MATRIX, K, results, node, visited):
    if len(solution) == K:
        ans = 0
        for sol in solution:
            ans += MATRIX[sol[0]][sol[1]]
        results.append(ans)
        return

    for row in range(node[0], len(MATRIX)):
        for col in range(node[1] if row == node[0] else 0, len(MATRIX[0])):
            if is_valid(solution, [row, col]) and not visited[row][col]:
                solution.append([row, col])
                visited[row][col] = True
                backtracking(solution, MATRIX, K, results, [row, col], visited)
                visited[row][col] = False
                solution.pop()


def main(MATRIX, N, M, K):
    """
    그리디로 접근할 수 없음 -> DP가 떠오름
    [i, j]는 현재의 칸, a_ij는 현재 칸에서 최대로 선택할 수 있는 총합이라고 생각
    [0, 0] -> MAT[0, 0]
    [1, 0] -> MAT[0, 0] OR MAT[1, 0]
    생각하긴 어렵지만 지금까지 지나온 값들 중 이웃을 제외한 MAX값을 a_max라고 하면,
    a_ij = max(a_max + a_ij, a_left, a_up)
    ...
    근데 K개만 딱 선택할 수 있어야 하는데? -> DP로는 떠오르지 않음
    선택했다가 되돌리는 방식은? -> 백트래킹
    """
    results = []
    visited = [[False] * M for _ in range(N)]
    backtracking([], MATRIX, K, results, [0, 0], visited)
    print(max(results))
    return


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    MATRIX = [list(map(int, input().split())) for _ in range(N)]
    main(MATRIX, N, M, K)

"""
신경쓰지 못했던 지점: 백트래킹은 낭비하는 탐색이 없어야 함
- visited 행렬 만들지 않은 것 -> 그래프 형태라면 원래 방문했던 곳을 다시 검토하는 게 의미 없음
- 탐색 시작 노드의 아래 부분, 오른쪽 부분만 탐색하면 된다는 것
"""
