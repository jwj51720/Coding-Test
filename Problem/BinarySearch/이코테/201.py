def main(N, M, TTEOK):
    # 1. 탐색 범위 설정
    # 이 문제에서는 절단기의 높이가 0부터 떡의 최대 길이(10억 이하만)까지 가능
    start, end = 0, min(max(TTEOK), 1000000000)
    # 2. 반복문 시작

    while start <= end:
        # 3. 중간 지점(현재 탐색 값) 설정
        mid = (start + end) // 2

        tteok_length = sum([t - mid for t in TTEOK if mid < t])

        # 4. 조건문 분기
        # 4-1. 목표 값을 찾은 경우
        # 이 문제에서는 딱 M만큼 남으면 더이상 높일 수 없으며, 낮추면 최적 값이 아니므로 바로 종료
        if tteok_length == M:
            break

        # 4-2. 중간점(현재 떡 길이)의 값보다 목표 값(M)이 작은 경우
        # 이 문제에서는 M 조건 만족하므로 절단기 높이를 올려봐야 함
        elif tteok_length > M:
            start = mid + 1

        # 4-3. 중간점(현재 떡 길이)의 값보다 목표 값(M)이 큰 경우
        # 이 문제에서는 M 조건 불만족하므로 절단기 높이를 내려야 함
        else:
            end = mid - 1
    print(mid)
    return


if __name__ == "__main__":
    N, M = map(int, input().split())
    TTEOK = list(map(int, input().split()))
    main(N, M, TTEOK)
