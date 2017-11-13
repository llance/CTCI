"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unrepeated_chars = []
        lengths = []

        for char in s:
            print("char is : ", char)
            if char not in unrepeated_chars:
                unrepeated_chars.append(char)
                print("unrepeated_chars is : ", unrepeated_chars)
            else:
                print("repeated_char is : ", char)
                lengths.append(len(unrepeated_chars))
                print("lengths is : ", lengths)
                del unrepeated_chars[:]
                unrepeated_chars.append(char)
                print("unrepeated_chars shuix is : ", unrepeated_chars)
        lengths.append(len(unrepeated_chars))

        if len(lengths) is not 0:
            for elem in lengths:
                print(elem)
            return max(lengths)
        elif len(lengths) is 0 and len(unrepeated_chars) is not 0:
            return len(unrepeated_chars)
        else:
            return 0


sol = Solution()

result = sol.lengthOfLongestSubstring("aab")

print(result)
