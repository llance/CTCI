__author__ = 'lanceli'
import unittest

def palindromePermatation(input_string):
    clean_input_string = input_string.replace(' ', '').upper()

    distinct_chars = get_distinct_chars(clean_input_string)

    distinct_char_count = dict((char,0) for char in clean_input_string)

    # print(distinct_char_count)


    if len(clean_input_string) % 2 == 0:
        for char in clean_input_string:
            if char in distinct_char_count.keys():
                distinct_char_count[char] += 1

        for key, value in distinct_char_count.items():
            if value%2 != 0:
                return False
        print(distinct_char_count)
        return True

    if len(clean_input_string) % 2 != 0:
        single_char_flag = False

        for char in clean_input_string:
            if char in distinct_char_count.keys():
                distinct_char_count[char] += 1

        for key, value in distinct_char_count.items():
            if value%2 != 0:
                if single_char_flag is True:
                    return False
                else:
                    single_char_flag = True
        print(distinct_char_count)
        return True






def get_distinct_chars(input_string):
    distinct_chars = []

    for char in input_string:
        if char not in distinct_chars:
            distinct_chars.append(char)
    return distinct_chars


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = palindromePermatation(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()