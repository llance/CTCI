class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        A_str_to_char = list(A)
        B_str_to_char = list(B)

        
        for i in range(0, len(A)):
            A_shifted = A_str_to_char[i+1: len(A)] + A_str_to_char[0:i+1]
            print("A_shifted is : ", A_shifted)
            print("B_str_to_char is : ", B_str_to_char)

            if (A_shifted == B_str_to_char):
                return True
            
        return False

if __name__ == "__main__":
    mysolx = Solution()
    mysolx.rotateString("abcde", "cdeab")