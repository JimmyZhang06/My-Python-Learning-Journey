"""用循环找出五个数中的最大值。"""


def mymax(a, b, c, d, e):
    numbers = [a, b, c, d, e]
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


if __name__ == "__main__":
    for numbers in [(1, 2, 3, 4, 5), (-8, -2, -5, -2, -9)]:
        print(f"输入：{numbers}")
        print(f"最大值：{mymax(*numbers)}")
