def complete_check(sequence, MATRIX, N):
    """해가 완성되었을 때 부호 조건을 만족하는지 확인하는 함수"""
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


def is_valid(sequence, MATRIX):
    """현재까지 완성된 부분 수열이 부호 행렬 조건을 역순으로 만족하는지 확인"""
    end = len(sequence) - 1
    s = 0
    for i in range(end, -1, -1):  # end부터 역순으로 합을 확인
        s += sequence[i]
        if MATRIX[i][end - i] == "+" and s <= 0:
            return False
        elif MATRIX[i][end - i] == "-" and s >= 0:
            return False
        elif MATRIX[i][end - i] == "0" and s != 0:
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
    for num in range(-10, 11):
        # 3. if statement: 유효한 후보인지 검사
        sequence.append(num)  # 후보 추가
        if is_valid(sequence, MATRIX):  # 후보가 유효한지 검사
            # 4. append/recurssive/pop: 후보 추가 후 재귀 호출
            if backtrack(sequence, MATRIX, N):  # 재귀 호출로 다음 값 탐색
                return True
        sequence.pop()  # 백트래킹: 후보 제거 후 다음 후보로


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
