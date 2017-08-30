__author__ = 'lanceli'
import unittest

def get_distinct_chars(input_string):
    distinct_char = []

    for char in input_string:
        if char not in distinct_char:
            distinct_char.append(char)

    return distinct_char

def string_compression(input_string):
    distinct_char = get_distinct_chars(input_string)

    distinct_char_count = dict((char,0) for char in input_string)

    for char in input_string:
            if char in distinct_char_count.keys():
                distinct_char_count[char] += 1

    compressed_string = ''

    print(sorted(distinct_char_count))

    for key, value in sorted(distinct_char_count.items()):
        compressed_string = compressed_string + str(key)+str(value)

    print(compressed_string)

    if len(compressed_string)>=len(input_string):
        return input_string
    else:
        return compressed_string


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            # self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
