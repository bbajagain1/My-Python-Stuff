import unittest
import cap

# testcase is created by subclassing unittest.TestCase
class TestCap(unittest.TestCase):
	
	#assertEqual() to check for an expected result;
	#assertTrue() or assertFalse() to verify a condition
	#assertRaises() to verify that a specific exception gets raised
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

# provides a command-line interface to the test script
if __name__ == '__main__':
		unittest.main()