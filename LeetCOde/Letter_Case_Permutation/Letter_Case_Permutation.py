class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if S is None:
            return [S]

        print(S)

        rest = self.letterCasePermutation(S[1:])

        if S[0].isalpha():
            return [S[0].upper() + rest] + [s[0] + rest]
        else:
            return s[0] + rest



if __name__ == "__main__":
    mysolx = Solution()
    mysolx.letterCasePermutation("a1b2")