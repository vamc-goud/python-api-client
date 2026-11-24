import unittest


def add(a, b):
    return a + b


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = add(10, 20)

        self.assertEqual(result, 30)


if __name__ == "__main__":
    unittest.main()