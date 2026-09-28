"""命令行入口：对比贪心与最优断行。"""

import argparse
import sys

from .wrap import WrapError, greedy, optimal


def build_parser():
    parser = argparse.ArgumentParser(prog="wrap-knuth", description="断行对照")
    parser.add_argument("--words", help="空格分隔的词")
    parser.add_argument("--width", type=int, default=8, help="行宽")
    parser.add_argument("--compare", action="store_true", help="同时给最优解")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        words = (args.words or "").split()
        lines, total = greedy(words, args.width)
    except WrapError as error:
        print("错误：%s" % error, file=sys.stderr)
        return 1
    print("greedy_lines=%d greedy_cost=%d" % (len(lines), total))
    print("greedy=%s" % "|".join(lines))
    if args.compare:
        best_lines, best_cost = optimal(words, args.width)
        print("optimal_lines=%d optimal_cost=%d" % (len(best_lines), best_cost))
        print("optimal=%s" % "|".join(best_lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
