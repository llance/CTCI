# S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

# S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

# Return any permutation of T (as a string) that satisfies this property.

# Example :
# Input: 
# S = "cba"
# T = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
# Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 

# Note:

# S has length at most 26, and no character is repeated in S.
# T has length at most 200.
# S and T consist of lowercase letters only.

import operator

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        s_dict = {}
        t_sorted = {}
        t_remain = []
        
        for  index, char in enumerate(S):
            s_dict[char] = index
            
        print('s_dict.keys are ', s_dict.keys())
        for char in T:
            if char in s_dict.keys():
                t_sorted[char] = s_dict[char]
                
            else:
                t_remain.append(char)
                
        print('t_sorted is : ', t_sorted)
                
        t_sorted_list = sorted(t_sorted.items(), key=operator.itemgetter(1))
        
        sorted_str = ''
        for elem in t_sorted_list:
            sorted_str += elem[0]
        print(sorted_str)
        
        return sorted_str + ''.join(t_remain)
