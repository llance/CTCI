# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_stack = []

        for index, char in enumerate(s):
            if (char == '(' or char == '[' or char == '{'):
                parentheses_stack.append(char)
            if (char == ')' and ( parentheses_stack == [] or parentheses_stack.pop() != '(')):
                return False
            if (char == ']' and ( parentheses_stack == [] or parentheses_stack.pop() != '[')):
                return False
            if (char == '}' and (parentheses_stack == [] or parentheses_stack.pop() != '{' )):
                return False           
        if len(parentheses_stack) != 0:
            return False     
        return True

if __name__ == '__main__':
    solx = Solution()
    solx.isValid('')