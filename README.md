# My-Python-Learning-Journey

## 项目简介

这个仓库记录本学期的两项 Python 课堂练习。一项从五个数中找出最大值，另一项根据尺寸计算圆形和矩形的面积与周长。

## 文件说明

- [`find_max.py`](find_max.py) 用两组示例演示如何求最大值，其中一组包含重复的负数。
- [`geometry_calculator.py`](geometry_calculator.py) 演示半径为 3 的圆形和宽 6、高 4 的矩形的计算结果。

## 代码说明

- `mymax()` 把第一个数作为当前最大值，循环比较剩余的数，遇到更大的值就更新。
- 几何脚本把面积和周长分别写成函数。圆形计算用 `math.pi` 取得圆周率，结果保留两位小数。

## 运行方法

在仓库目录使用 Python 3 运行以下命令。两个程序都只用到 Python 自带的功能。

```powershell
python find_max.py
python geometry_calculator.py
```

## 学习心得与规划

[Requests 的 README](https://github.com/psf/requests/blob/main/README.md) 在开头用几行代码展示了库怎么用，还列出了安装方法。我也想让别人打开我的仓库后，能马上找到程序、试着运行，并看懂我用循环或函数解决了什么问题。整理课堂练习时，我把混在同一个文件里的求最大值代码单独放了出来，并加了一组全为负数的例子，检查循环是否仍能找到正确结果。

以后每完成一个单元，我计划选一个能独立运行的练习上传，写清楚输入和预期输出，再用一句具体的提交说明记录改动。学到 Pandas 后，我想用模拟数据做一个学习时长统计练习，并在 README 里补上运行方法和结果示例。
