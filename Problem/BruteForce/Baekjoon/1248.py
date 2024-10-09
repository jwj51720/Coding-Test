def complete_check(sequence, MATRIX, N):
    for i in range(N):
        total = 0
        for j in range(i, N):
            total += sequence[j]
            # 부호 행렬의 조건을 검사
            if MATRIX[i][j - i] == "+" and total <= 0:
                return False
            elif MATRIX[i][j - i] == "-" and total >= 0:
                return False
            elif MATRIX[i][j - i] == "0" and total != 0:
                return False
    return True


def backtrack(sequence, MATRIX, N):
    # 1. Base Case: 해가 완성되었는지 확인
    if len(sequence) == N:
        if complete_check(sequence, MATRIX, N):
            print(" ".join(map(str, sequence)))
            return True
        return False

    # 2. for loop: -10부터 10까지의 수들을 시도
    # ** 탐색 범위 최적화: 부호 행렬에 따라 값 선택
    idx = len(sequence)
    if MATRIX[idx][0] == "+":
        candidates = range(1, 11)  # 양수만 탐색
    elif MATRIX[idx][0] == "-":
        candidates = range(-10, 0)  # 음수만 탐색
    else:
        candidates = [0]  # 0만 탐색

    for num in candidates:
        sequence.append(num)  # 후보 추가
        if backtrack(sequence, MATRIX, N):  # 재귀 호출
            # 여기선 하나만 출력하고 바로 탈출해야 해서
            # 드물게 종료 조건 넣음
            return True
        sequence.pop()  # 백트래킹: 선택을 되돌림


def main(N, MATRIX):
    # Solution: sequence
    # current_state: MATRIX
    sequence = []
    backtrack(sequence, MATRIX, N)  # 백트래킹 시작


if __name__ == "__main__":
    N = int(input())
    MAT = [n for n in input()]
    MATRIX = [[] * N for _ in range(N)]
    k = 0
    for i in range(N, 0, -1):
        MATRIX[N - i] = MAT[k : k + i]
        k = k + i
    main(N, MATRIX)
