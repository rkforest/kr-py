import unittest
import temp_converter as tc

class TestStringMethods(unittest.TestCase):

    def test_zero_c_f(self):
        test = [0, 'c', 'f']
        expected = 32
        result = tc.temp_converter(test[0], test[1], test[2])
        self.assertEqual(result, expected)

    def test_zero_k_c(self):
        test = [0, 'k', 'c']
        expected = -273.15
        result = tc.temp_converter(test[0], test[1], test[2])
        self.assertEqual(result, expected)

    def test_zero_f_c(self):
        test = [32, 'f', 'c']
        expected = 0
        result = tc.temp_converter(test[0], test[1], test[2])
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()