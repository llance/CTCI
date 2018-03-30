class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        J_list = list(J)
        S_list = list(S)
        count=0
        for stone in S_list:
            if stone in J_list:
                count +=1
        return count
        