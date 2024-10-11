from collections import deque

def BFS(M,N,MIRO):
    visited = [[-1] * M for _ in range(N)]
    
    queue = deque([[0,0]])
    visited[0][0] = 0
    
    while queue:
        v = queue.popleft()
        row, col = v[0], v[1]
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, 1, -1]):
            nr, nc = row + dr, col + dc
            if nr in range(N) and nc in range(M) and visited[nr][nc] == -1:
                if MIRO[nr][nc] == 0:
                    visited[nr][nc] = visited[row][col]
                    queue.appendleft([nr, nc]) # queue의 왼쪽에 넣어 우선순위 부여
                else:
                    visited[nr][nc] = visited[row][col] + 1
                    queue.append([nr, nc]) # queue의 오른쪽에 넣어 갈 곳 없을 때 처리
    print(visited[-1][-1])

def main(M,N,MIRO):
    """
    최단 경로를 구하는 전형적인 BFS
    단, 다음 칸이 0이라면 CNT를 늘리지 않고, 1이라면 늘리자.
    
    벽도 뚫을 수 있다는 점에서, 일반적인 BFS가 가지고 있는 제약(벽보다 길이 무조건 우선)이 사라짐
    하지만 여전히 길로만 가는 게 최소의 벽 뚫기 횟수를 기록하는 방법이므로
    길을 우선적으로 선택할 수 있게 queue에 담는 방식으로 조절
    """
    BFS(M,N,MIRO)
    return


if __name__ == "__main__":
    M, N = map(int, input().split())
    MIRO = [[int(k) for k in input()] for _ in range(N)]
    main(M,N,MIRO)
