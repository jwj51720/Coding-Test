from itertools import combinations


def backtrack_combinations(solution, nums, start, length, results):
    if len(solution) == length:
        results.append(solution[:])  # 현재 조합을 결과 리스트에 추가
        return

    for i in range(start, len(nums)):  # 시작 지점 잘 보기
        candidate = nums[i]
        solution.append(candidate)  # 후보 선택
        backtrack_combinations(solution, nums, i + 1, length, results)  # 재귀 호출
        solution.pop()  # 백트래킹: 선택을 되돌림


def backtracking_impl(K, NUMS):
    results = []
    backtrack_combinations([], NUMS, 0, 6, results)
    for result in results:
        for r in result:
            print(r, end=" ")
        print()
    return


def main(K, NUMS):
    for comb in combinations(NUMS, 6):
        for c in comb:
            print(c, end=" ")
        print()
    return


if __name__ == "__main__":
    while True:
        input_str = input()
        if input_str == "0":
            break
        NUMS = list(map(int, input_str.split()))
        K = NUMS.pop(0)
        backtracking_impl(K, NUMS)
        print()
