__author__ = 'lanceli'
import unittest
from collections import Counter


def checkIfPermutation(string1, string2):
    if len(string1) != len(string2):
        return False

    counter = Counter()

    for char in string1:
        print("char is :", char)

        if char not in string2 :
            return False
        else :
            counter[char] += 1

    for char in counter:
        print("counter[", char, "] is ", counter[char])
        if counter[char] != 1:
            return False
    return True



class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = checkIfPermutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = checkIfPermutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
