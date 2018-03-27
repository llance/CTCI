# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        t = list(s)
        
        for index, char in enumerate(s):
            # print(index)
            # if index == 0:
            #     print(s[index:k][::-1])
                
            if (index % (2*k) == 0):
                # print('every 2k at index = ', index)
                # s[index:k] = s[index:k][::-1]
                # print(s[index:index+k][::-1][1])
                
                for i in range(index, index+k-1):
                    # print('k-(i+1) is :' , k-(i+1))
                    # print( s[index:index+k][::-1][k-(i+1)])
                    t[index:index+k] = s[index:index+k][::-1]
        print(t)
        return ''.join(t)
        