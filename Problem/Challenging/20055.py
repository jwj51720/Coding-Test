from collections import deque


def main(N, K, A):
    while True:
        A.rotate(1)
    print(N, K, A)
    pass


if __name__ == "__main__":
    N, K = map(int, input().split())
    A = deque(map(int, input().split()))
    main(N, K, A)
