"""计算圆形和矩形的面积与周长。"""

import argparse
import math


def circle_area(radius):
    return round(math.pi * radius * radius, 2)


def circle_perimeter(radius):
    return round(2 * math.pi * radius, 2)


def rectangle_area(width, height):
    return width * height


def rectangle_perimeter(width, height):
    return 2 * (width + height)


def main():
    parser = argparse.ArgumentParser(description="计算圆形和矩形的面积与周长。")
    parser.add_argument("--radius", type=float, default=3.0, help="圆形半径，默认 3。")
    parser.add_argument("--width", type=float, default=6.0, help="矩形宽度，默认 6。")
    parser.add_argument("--height", type=float, default=4.0, help="矩形高度，默认 4。")
    args = parser.parse_args()

    radius, width, height = args.radius, args.width, args.height
    if any(not math.isfinite(length) or length <= 0 for length in (radius, width, height)):
        parser.error("半径、宽度和高度都必须是有限的正数。")

    circle_a = circle_area(radius)
    circle_p = circle_perimeter(radius)
    rectangle_a = rectangle_area(width, height)
    rectangle_p = rectangle_perimeter(width, height)
    if any(not math.isfinite(value) for value in (circle_a, circle_p, rectangle_a, rectangle_p)):
        parser.error("尺寸过大，计算结果超出可表示的范围。")

    print(f"圆形（半径 {radius:g}）")
    print(f"面积：{circle_a:.2f}，周长：{circle_p:.2f}")
    print(f"矩形（宽 {width:g}，高 {height:g}）")
    print(f"面积：{rectangle_a:.2f}，周长：{rectangle_p:.2f}")


if __name__ == "__main__":
    main()
