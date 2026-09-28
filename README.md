# wrap-knuth

文本断行：贪心与 Knuth 最优 DP，只用 Python 标准库。

```
python3 -m wrapknuth.cli --words 'aaa bb cc ddddd' --width 6 --compare
python3 -m unittest discover -s tests -v
```

## 口径（README 为准）

- **惩罚要用 slack 的立方**（末行不计）：`penalty(slack) = slack ** 3`。现在只用一次方，
  所以任何断法的代价都算不对。
- **最优解要真的做 DP**：`optimal(words, width)` 用 `best[i] = min(best[j] + penalty(slack))`
  在 O(n²) 里求最小总惩罚并回溯断点；现在 `optimal` 直接返回贪心结果，
  `--words 'aaa bb cc ddddd' --width 6 --compare` 会给出两条完全一样的行。
- 不变量：`optimal` 的代价 ≤ `greedy` 的代价；最优解所有中间行长度 ≤ width（末行不罚但不许超宽）；
  同一输入重复求解给出同样的断点；词序不变（不许重排或丢词）。
- 边界：空词表给空行、代价 0；单词比 width 长报 `WrapError`；width ≤ 0 报错。
- 规模：10^5 个词、width = 80 要在 2 秒内给出最优断点，内存 O(n)。

## 现在的行为

- `penalty` 返回 `slack`（一次方），不是立方。
- `optimal` 直接 `return greedy(words, width)`：没有 DP，也就没有最优性。
- 贪心与代价累计的框架是对的，所以 `--compare` 里两行输出一模一样。

## 计划新增的能力

```
--words 词表     空格分隔
--width N        行宽
--compare        同时给最优解
```

## 输出

```
greedy_lines=3 greedy_cost=64
greedy=aaa bb|cc|ddddd
optimal_lines=3 optimal_cost=28
optimal=aaa|bb cc|ddddd
```

## 目录

```
wrapknuth/wrap.py    贪心、DP 与代价
wrapknuth/cli.py     命令行入口
tests/               unittest 用例
```
