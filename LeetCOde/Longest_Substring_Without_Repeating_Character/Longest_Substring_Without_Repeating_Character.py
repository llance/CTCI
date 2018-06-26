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
        if s == "":
            return 0

        longest_substring = []
        lenghts = []
        for char in s:
            # print("char is : ", char)
            if char not in longest_substring:
                longest_substring.append(char)
            elif longest_substring[-1] == char:
                lenghts.append(len(longest_substring))
                longest_substring = [char]
            else:
                lenghts.append(len(longest_substring))
                longest_substring = longest_substring[longest_substring.index(char)+1:]
                longest_substring.append(char)
            # print("longest_substring is : ", longest_substring)
        if len(longest_substring) != 0:
            lenghts.append(len(longest_substring))
            
        # print(lenghts)
        
        return max(lenghts)


sol = Solution()

result = sol.lengthOfLongestSubstring("aab")

print(result)
