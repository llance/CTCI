
# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]
# Note:

# S will be a string with length at most 12.
# S will consist only of letters or digits.



class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        output = []
        true_output = []
        alpha_count = 0
        for index, elem in enumerate(S):
            if elem.isalpha():
                alpha_count += 1
                if len(output) == 0:
                    output.append([elem])
                    output.append([elem.upper()])
                else:


                    for perm in list(output):
                        print('permutation is : ', perm)
                        copy_of_lower_perm = list(perm)
                        copy_of_lower_perm.append(elem)

                        copy_of_upper_perm = list(perm)
                        copy_of_upper_perm.append(elem.upper())
                        output.append(copy_of_lower_perm)
                        output.append(copy_of_upper_perm)
                    
                        print('output is : ', output)

            else:
                for perm in output:
                    perm.append(elem)

        for elem in output: 
            if len(elem) == (alpha_count * 2):
                true_output.append(''.join(elem))

        print('final output is : ', true_output)


        return true_output


if __name__ == "__main__":
    mysolx = Solution()
    mysolx.letterCasePermutation("a1b2c3")