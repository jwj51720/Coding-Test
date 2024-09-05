def main(A, B, C):
    print(
        (A + B) % C,
        ((A % C) + (B % C)) % C,
        (A * B) % C,
        ((A % C) * (B % C)) % C,
        sep="\n",
    )
    return


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    main(A, B, C)
