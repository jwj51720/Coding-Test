# 음료수 얼려먹기
from collections import deque


def main(N, M, FRAME):
    # 1. visited 만들기
    visited = [[False] * M for _ in range(N)]

    count = 0
    # 2. 시작 노드 Queue에 삽입 & 방문 처리
    # 이 문제에서는 시작 지점을 계속 반복하면서 찾아야 함
    for i in range(N):  # 행
        for j in range(M):  # 열
            if FRAME[i][j] == 0 and not visited[i][j]:
                queue = deque([[i, j]])
                visited[i][j] = True
                count += 1

                # 3. bfs while 반복문 제작
                while queue:
                    # 3-1. Queue에서 노드 하나 꺼냄
                    v = queue.popleft()
                    row, col = v[0], v[1]
                    # 3-2. 문제에서 원하는 작동
                    # 이 문제에서는 dfs 내부에서 원하는 작동 없음

                    # 3-3. 인접 노드(상, 하, 좌, 우) Queue에 삽입 & 방문 처리
                    for dr, dl in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                        new_row, new_col = row + dr, col + dl
                        if new_row in range(N) and new_col in range(M):
                            if (
                                FRAME[new_row][new_col] == 0
                                and not visited[new_row][new_col]
                            ):
                                queue.append([new_row, new_col])
                                visited[new_row][new_col] = True

    print(count)
    return


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    FRAME = [[int(i) for i in input()] for _ in range(N)]
    main(N, M, FRAME)
