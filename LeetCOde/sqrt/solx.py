class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        sqrt=str(x**(1/2))
        
        print(sqrt)
        
        if sqrt.find('.') != -1:
            return int(sqrt[:sqrt.find('.')])
        else: 
            return int(sqrt)