from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
box = [list(map(int, stdin.readline().split())) for _ in range(N)]


def findtomato(n):
    list = deque()
    for i in range(N):
        for j in range(M):
            if box[i][j] == n:
                list.append([i, j])
    return list


def spread():
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = findtomato(1)

    while queue:
        x = queue.popleft()
        for m in move:
            if 0 <= x[0] + m[0] < N and 0 <= x[1] + m[1] < M:
                if box[x[0] + m[0]][x[1] + m[1]] == 0:
                    box[x[0] + m[0]][x[1] + m[1]] = box[x[0]][x[1]] + 1
                    queue.append([x[0] + m[0], x[1] + m[1]])


spread()
if findtomato(0):
    print(-1)
else:
    maxday = 0
    for i in box:
        for j in i:
            maxday = max(maxday, j)
    print(maxday - 1)
