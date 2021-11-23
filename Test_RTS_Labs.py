import unittest

from RTS_Labs import RTSLabsChallenge


class AboveBelowTests(unittest.TestCase):
    def test_given_test(self):
        self.assertEqual(
            RTSLabsChallenge.aboveBelow(
                [1, 5, 2, 1, 10],
                6
            ),
            {"above": 1, "below": 4}
        )

    def test_includes_number(self):
        self.assertEqual(
            RTSLabsChallenge.aboveBelow(
                [1, 5, 2, 1, 10, 6, 6],
                6
            ),
            {"above": 1, "below": 4}
        )

    def test_only_input_number(self):
        self.assertEqual(
            RTSLabsChallenge.aboveBelow(
                [6, 6, 6, 6, 6, 6, 6, 6],
                6
            ),
            {"above": 0, "below": 0}
        )


class AboveBelowEqualsTests(unittest.TestCase):
    def test_given_test(self):
        self.assertEqual(
            RTSLabsChallenge.aboveBelowEqual(
                [1, 5, 2, 1, 10],
                6
            ),
            {"above": 1, "below": 4, "equal": 0}
        )

    def test_includes_number(self):
        self.assertEqual(
            RTSLabsChallenge.aboveBelowEqual(
                [1, 5, 2, 1, 10, 6, 6],
                6
            ),
            {"above": 1, "below": 4, "equal": 2}
        )

    def test_only_input_number(self):
        self.assertEqual(
            RTSLabsChallenge.aboveBelowEqual(
                [6, 6, 6, 6, 6, 6, 6, 6],
                6
            ),
            {"above": 0, "below": 0, "equal": 8}
        )


class StringRotationTests(unittest.TestCase):
    def test_given_test(self):
        self.assertEqual(
            RTSLabsChallenge.stringRotation("MyString", 2),
            "ngMyStri"
        )

    def test_greater_than_length(self):
        self.assertEqual(
            RTSLabsChallenge.stringRotation("MyString", len("MyString") + 2),
            "ngMyStri"
        )

    def test_really_big_number(self):
        self.assertEqual(
            RTSLabsChallenge.stringRotation("MyString", 200000000002),
            "ngMyStri"
        )

    def test_for_negative_number(self):
        self.assertRaises(ValueError, RTSLabsChallenge.stringRotation, "MyString", -10)

    def test_for_empty_string(self):
        self.assertEqual(
            RTSLabsChallenge.stringRotation("", 2),
            ""
        )


if __name__ == '__main__':
    unittest.main()
