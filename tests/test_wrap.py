import unittest

from wrapknuth.wrap import WrapError, cost, greedy, penalty


class CheckTest(unittest.TestCase):
    def test_bad_width(self):
        with self.assertRaises(WrapError):
            greedy(["a"], 0)

    def test_long_word(self):
        with self.assertRaises(WrapError):
            greedy(["abcdef"], 3)


class GreedyTest(unittest.TestCase):
    def test_single_line(self):
        lines, _ = greedy(["aa", "bb"], 10)
        self.assertEqual(lines, ["aa bb"])

    def test_wraps_when_needed(self):
        lines, _ = greedy(["aa", "bb", "cc"], 5)
        self.assertEqual(lines, ["aa bb", "cc"])

    def test_cost_ignores_last_line(self):
        self.assertEqual(cost(["aa", "bb"], 5), 3)

    def test_penalty_is_positive(self):
        self.assertGreater(penalty(3), 0)


if __name__ == "__main__":
    unittest.main()
