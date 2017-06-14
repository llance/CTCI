__author__ = 'lanceli'
import unittest

def check_One_Away(string1, string2):
    len_string1 = len(string1)
    len_string2 = len(string2)

    if abs(len_string1-len_string2) > 1:
        return False

    if abs(len_string1-len_string2) == 1 or abs(len_string1-len_string2) == 0 :
        if len_string1 >= len_string2:
            for char in string2:
                string1 = string1.replace(char, '')

            print(string1, string2)
            if len(string1) > 1:
                return False
            else:
                return True
        if len_string2 > len_string1:
            for char in string1:
                string2 = string2.replace(char, '')
            print(string2, string1)
            if len(string2) > 1:
                return False
            else:
                return True



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = check_One_Away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
