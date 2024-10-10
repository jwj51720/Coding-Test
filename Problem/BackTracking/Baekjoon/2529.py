def is_valid(current_num, current_sign, i):
    if current_sign == "<":
        return current_num < i
    else:
        return current_num > i


def backtracking(solution, SIGN, results):
    if len(solution) == len(SIGN) + 1:
        results.append("".join(map(str, solution)))
        return
    current_num = solution[-1]
    current_sign = SIGN[len(solution) - 1]
    for i in range(0, 10):
        if is_valid(current_num, current_sign, i) and i not in solution:
            solution.append(i)
            backtracking(solution, SIGN, results)
            solution.pop()


def main(K, SIGN):
    """
    경우의 수가 아주 많아서 하나를 선택한 다음의 선택이 어떨지 검증하고, 되돌리기
    그렇다면 백트래킹
    단, 가장 클 때, 가장 작을 때를 나눠서 봐야 하기 때문에 중간 부분은 안 봐도 됨
    최대한 효율적인 탐색을 하도록 건너 뛸 수 있게 함
    """
    for i in range(9, -1, -1):
        solution = [i]
        results = []
        backtracking(solution, SIGN, results)
        if results:
            print(results[-1])
            break

    for i in range(10):
        solution = [i]
        results = []
        backtracking(solution, SIGN, results)
        if results:
            print(results[0])
            break


if __name__ == "__main__":
    K = int(input())
    SIGN = list(input().split())
    main(K, SIGN)
