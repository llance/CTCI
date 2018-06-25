class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while len(str(num)) > 1:    
            sum = 0
            for digit in str(num):
                sum += int(digit)
            num = str(sum)
            print ("num is : ", num)
        return int(num)