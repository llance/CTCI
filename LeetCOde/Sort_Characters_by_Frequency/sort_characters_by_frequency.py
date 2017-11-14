from collections import defaultdict


class Solution:

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_frequency = defaultdict(int)

        for char in s:
            # print(char_frequency[str(char)])
            char_frequency[str(char)] += 1

        # for key, value in char_frequency.iteritems():
            # print('char_frequency[%s]:%s' % (key, value))

        chars_sorted_by_frequency = ""

        # for key, value in char_frequency.iteritems():

        for key, value in sorted(char_frequency.iteritems(), key=lambda(k, v): (v, k), reverse=True):
            # print "%s: %s" % (key, value)
            chars_sorted_by_frequency += value * str(key)

        print("chars_sorted_by_frequency is : %s" % (chars_sorted_by_frequency))

        return chars_sorted_by_frequency
