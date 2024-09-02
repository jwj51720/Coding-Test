# 음료수 얼려먹기
def main(N, M, FRAME):
    # 3. dfs 재귀 함수 제작
    def dfs(graph, v, visited):
        # 3-1. 노드 방문 처리
        row, col = v[0], v[1]
        visited[row][col] = True

        # 3-2. 문제에서 원하는 작동
        # 이 문제에서는 dfs 내부에서 원하는 작동 없음

        # 3-3. 인접 노드(상, 하, 좌, 우) Stack에 삽입 & 꺼냄
        for dr, dl in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            new_row, new_col = row + dr, col + dl
            if new_row in range(N) and new_col in range(M):
                if graph[new_row][new_col] == 0 and not visited[new_row][new_col]:
                    dfs(graph, [row + dr, col + dl], visited)

        # 3-4. 종료 조건
        # 종료 조건은 보통 앞에 있으나 이렇게 필요 없을 수도
        return  # 인접 노드(상, 하, 좌, 우) 갈 곳 없으면 자연스럽게 종료

    # 1. visited 만들기
    visited = [[False] * M for _ in range(N)]

    count = 0
    # 2. 시작 노드 Stack에 삽입 & 꺼냄
    # 이 문제에서는 시작 지점을 계속 반복하면서 찾아야 함
    for i in range(N):  # 행
        for j in range(M):  # 열
            if FRAME[i][j] == 0 and not visited[i][j]:
                dfs(FRAME, [i, j], visited)
                count += 1

    print(count)
    return


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    FRAME = [[int(i) for i in input()] for _ in range(N)]
    main(N, M, FRAME)
