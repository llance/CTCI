__author__ = 'lanceli'
import unittest

def urlify(input, inputlength):
    output = ""

    for index, char in enumerate(input):
        print("index is : ", index)
        if index >= inputlength:
            print("output is : ", output)

            return str(output)
        if char == " ":
            output = output + "%20"
        else:
            output = output + char
    return str(output)

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         'much%20ado%20about%20nothing'),
        (list('Mr John Smith    '), 13, 'Mr%20John%20Smith')]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()