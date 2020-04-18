import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, 1)

    def test_demo(self):
        a = 1
        b = 1
        self.assertEqual(a, b, 'not equal')


if __name__ == '__main__':
    unittest.main()
