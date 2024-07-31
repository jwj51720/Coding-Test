def find_tomato(box):
    first_tomato_location = []
    for r, row in enumerate(box):
        for c, col in enumerate(row):
            if col == 1:
                first_tomato_location.append([r, c])
    return first_tomato_location


def ripe(row, col, box):
    next_tomato_location = []
    for dx, dy in [[1, 0], [0, -1], [-1, 0], [0, 1]]:
        if (row + dx) in range(len(box)) and (col + dy) in range(len(box[0])):  # 정상 범위
            if box[row + dx][col + dy] == 0:  # 익지 않은 토마토 존재
                next_tomato_location.append([row + dx, col + dy])
                box[row + dx][col + dy] = 1
    return next_tomato_location


def main(M, N, box):
    # 토마토가 어디에 있는지 찾기
    tomato_location = find_tomato(box)  # 익은 토마토의 좌표
    day = 0
    if not tomato_location:  # 익은 토마토가 없으면 반환
        print(-1)
        return -1
    while True:
        next_tomato_location = []  # 다음 토마토
        while tomato_location:
            row, col = tomato_location.pop()  # 익은 토마토를 하나씩 꺼냄
            next_tomato_location.extend(
                ripe(row, col, box)
            )  # 익은 토마토의 주변 토마토를 다음 토마토에 넣음
        if not next_tomato_location:  # 주변 토마토가 없음
            if any(0 in row for row in box):  # 안 익은 토마토가 존재
                print(-1)
                return -1
            else:  # 모두 익었음
                print(day)
                return day
        tomato_location = next_tomato_location  # 토마토 위치 <- 다음 토마토
        day += 1


if __name__ == "__main__":
    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    main(M, N, box)
