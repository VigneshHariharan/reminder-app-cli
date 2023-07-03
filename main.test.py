import unittest

class TestInputPrompts(unittest.TestCase):
    def test_inputFormat(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()