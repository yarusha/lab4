import sys


def add(a, b) -> int:
    return a + b


def main(arg1: str, arg2: str):
    num1 = int(arg1)
    num2 = int(arg2)
    # print(add(num1, num2))
    sys.stdout.write(str(add(num1, num2)) + "\n")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python add.py num1 num2")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
