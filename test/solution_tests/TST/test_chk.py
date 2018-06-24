import unittest

from solutions.CHK import checkout_solution


class TestSum(unittest.TestCase):
    def test_chk(self):
        self.assertEqual(checkout_solution.checkout("AAAAAA"), 250)
        self.assertEqual(checkout_solution.checkout("AAAAAAAA"), 330)
        self.assertEqual(checkout_solution.checkout("PPPPPPPPPP"), 400)
        self.assertEqual(checkout_solution.checkout("SSS"), 45)
        # self.assertEqual(checkout_solution.checkout("SSSS"),65)
        self.assertEqual(checkout_solution.checkout("S"), 20)
        self.assertEqual(checkout_solution.checkout("X"), 17)
        self.assertEqual(checkout_solution.checkout("Z"), 21)
        self.assertEqual(checkout_solution.checkout("TTTSSS"), 90)
        self.assertEqual(checkout_solution.checkout("LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH"), 1602)


if __name__ == '__main__':
    unittest.main()
