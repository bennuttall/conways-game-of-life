import unittest


class Test(unittest.TestCase):
    def test_1(self):
        a = 1
        b = 2

        ans = adder(a, b)
        expected = 3
        self.assertEqual(ans, expected)
    
    def test_2(self):
        a = 2
        b = 2

        ans = adder(a, b)
        expected = 4
        self.assertEqual(ans, expected)

def adder(a, b):
    return 3

if __name__ == '__main__':
    unittest.main()
