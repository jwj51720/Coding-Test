# 미로 탈출
from collections import deque


def main(N, M, MIRO):
    # 1. visited 만들기
    visited = [[0] * M for _ in range(N)]

    # 2. 시작 노드 Queue에 삽입 & 방문 처리
    queue = deque([[0, 0]])
    visited[0][0] = 1

    # 3. bfs while 반복문 제작
    while queue:
        # 3-1. Queue에서 노드 하나 꺼냄
        v = queue.popleft()
        row, col = v[0], v[1]
        # 3-2. 문제에서 원하는 작동
        # 이 문제에서는 bfs 내부에서 원하는 작동 없음

        # 3-3. 인접 노드(상, 하, 좌, 우) Queue에 삽입 & 방문 처리
        for dr, dl in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            new_row, new_col = row + dr, col + dl
            if new_row in range(N) and new_col in range(M):
                if MIRO[new_row][new_col] == 1 and visited[new_row][new_col] == 0:
                    queue.append([new_row, new_col])
                    visited[new_row][new_col] = visited[row][col] + 1

    print(visited[-1][-1])


if __name__ == "__main__":
    N, M = map(int, input().split())
    MIRO = [[int(i) for i in input()] for _ in range(N)]
    main(N, M, MIRO)
