import unittest

def function_that_returns_none():
    return None

class TestFunctions(unittest.TestCase):

    def test_function_returns_none(self):
        result = function_that_returns_none()
        self.assertIsNone(result, "The function should return None")

if __name__ == '__main__':
    unittest.main()