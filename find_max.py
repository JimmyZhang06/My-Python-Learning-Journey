"""用循环找出五个整数中的最大值。"""

import argparse


def mymax(a, b, c, d, e):
    """依次比较后四个数，返回当前找到的最大值。"""
    largest = a
    for number in (b, c, d, e):
        if number > largest:
            largest = number
    return largest


def main():
    parser = argparse.ArgumentParser(description="用循环找出五个整数中的最大值。")
    parser.add_argument("numbers", nargs="*", type=int, metavar="整数", help="输入五个整数。不输入时运行两组示例。")
    args = parser.parse_args()

    if args.numbers and len(args.numbers) != 5:
        parser.error("请输入恰好五个整数，或省略参数以运行示例。")

    examples = [(1, 2, 3, 4, 5), (-8, -2, -5, -2, -9)]
    groups = [tuple(args.numbers)] if args.numbers else examples
    for numbers in groups:
        print(f"输入：{numbers}")
        print(f"最大值：{mymax(*numbers)}")


if __name__ == "__main__":
    main()
