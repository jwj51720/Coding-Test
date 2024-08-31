# 음료수 얼려먹기
def main_dfs(N, M, FRAME):
    # 1. visited와 Stack 만들기
    visited = [[False] * M for _ in range(N)]

    # 3. dfs 재귀 함수 제작
    def dfs(graph, v, visited):
        # 2-1. 시작 노드 방문 처리
        row, col = v[0], v[1]
        visited[row][col] = True

        # 2-2. 문제에서 원하는 작동

        # 2-3. 인접 노드(상, 하, 좌, 우) 순서대로 dfs 재귀
        for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            new_row, new_col = row + i, col + j
            if new_row in range(N) and new_col in range(M):
                if graph[new_row][new_col] == 0 and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    dfs(graph, [row + i, col + j], visited)

        # 2-4. 종료 조건
        return

    count = 0
    # 2. 탐색 시작 노드 생성 & Stack에 삽입 및 방문 처리
    for i in range(N):  # 행
        for j in range(M):  # 열
            if FRAME[i][j] == 0 and not visited[i][j]:
                visited[i][j] = True
                dfs(FRAME, [i, j], visited)
                count += 1

    print(count)
    return


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    FRAME = [[int(i) for i in input()] for _ in range(N)]
    main_dfs(N, M, FRAME)
