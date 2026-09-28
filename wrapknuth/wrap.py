"""文本断行：贪心与 Knuth 最优 DP，只用标准库。

缺陷：optimal 直接返回贪心结果；惩罚函数用 slack 而不是 slack 的立方。
"""


class WrapError(ValueError):
    """输入不合法。缺陷：不带词下标。"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


def _check(words, width):
    if width <= 0:
        raise WrapError("宽度必须为正")
    for word in words:
        if len(word) > width:
            raise WrapError("单词比宽度还长：%s" % word)


def penalty(slack):
    """缺陷：应该是 slack 的立方（末行不计惩罚），现在只用一次方。"""
    return slack


def cost(lines, width):
    """非末行的惩罚之和。"""
    total = 0
    for line in lines[:-1]:
        total += penalty(width - len(line))
    return total


def greedy(words, width):
    """贪心：能塞就塞。"""
    _check(words, width)
    lines = []
    current = []
    length = 0
    for word in words:
        extra = len(word) if not current else len(word) + 1
        if length + extra <= width:
            current.append(word)
            length += extra
        else:
            lines.append(" ".join(current))
            current = [word]
            length = len(word)
    if current:
        lines.append(" ".join(current))
    return lines, cost(lines, width)


def optimal(words, width):
    """缺陷：直接返回贪心结果，没有做 DP。"""
    return greedy(words, width)
