def main(N):
    # 3kg, 5kg
    n1 = N // 5
    _n1 = N % 5
    if _n1 == 0:
        print(n1)
        return 
    for i in range(n1, -1, -1):
        res = N - i * 5
        n2 = res // 3
        _n2 = res % 3
        if _n2 == 0:
            print(i + n2)
            return 
    print(-1)
    return
            

if __name__ == "__main__":
    N = int(input())
    main(N)