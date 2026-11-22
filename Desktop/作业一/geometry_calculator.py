"""计算圆形和矩形的面积与周长。"""

import math


def circle_area(radius):
    return round(math.pi * radius ** 2, 2)


def circle_perimeter(radius):
    return round(2 * math.pi * radius, 2)


def rectangle_area(width, height):
    return width * height


def rectangle_perimeter(width, height):
    return 2 * (width + height)


if __name__ == "__main__":
    radius = 3
    width, height = 6, 4

    print(f"圆形（半径 {radius}）")
    print(f"面积：{circle_area(radius):.2f}，周长：{circle_perimeter(radius):.2f}")

    print(f"矩形（宽 {width}，高 {height}）")
    print(f"面积：{rectangle_area(width, height)}，周长：{rectangle_perimeter(width, height)}")
