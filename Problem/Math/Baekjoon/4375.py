def main(TEST):
    answer = []
    for num in TEST:
        target = "1"
        while int(target) % num:
            target += "1"
        answer.append(len(target))
    for a in answer:
        print(a)


if __name__ == "__main__":
    TEST = []
    try:
        while True:
            num = int(input())
            TEST.append(num)
    except EOFError:
        pass
    main(TEST)
