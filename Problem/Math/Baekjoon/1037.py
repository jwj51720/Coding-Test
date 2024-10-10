from collections import Counter


def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n


def lcm(n, m):
    return n * m / gcd(n, m)


def main(DIVISOR_NUM, DIVISOR):
    lcm_num = 1
    for d in DIVISOR:
        lcm_num = lcm(lcm_num, d)
    if lcm_num in DIVISOR:
        lcm_num *= min(DIVISOR)
    print(int(lcm_num))
    return


if __name__ == "__main__":
    DIVISOR_NUM = int(input())
    DIVISOR = list(map(int, input().split()))
    main(DIVISOR_NUM, DIVISOR)
