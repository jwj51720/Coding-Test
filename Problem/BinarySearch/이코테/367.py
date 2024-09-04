# 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right


def main(N, x, ARRAY):
    def count_by_range(a, left_value, right_value):
        right_index = bisect_right(a, right_value)
        left_index = bisect_left(a, left_value)
        return right_index - left_index

    # 값이 [x, x]인 데이터 개수 출력
    count = count_by_range(ARRAY, x, x)
    if count == 0:
        print(-1)
    else:
        print(count)
    return


if __name__ == "__main__":
    N, x = map(int, input().split())
    ARRAY = list(map(int, input().split()))
    main(N, x, ARRAY)
