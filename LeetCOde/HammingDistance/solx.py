class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # x_bin = str("{0:b}".format(x))
        x_bin = str(format(x, '032b'))
        y_bin = str(format(y, '032b'))
        print('x_bin is : ', x_bin)
        print('y_bin is : ', y_bin)
        
        hemming_distance = 0
        
        for key, val in enumerate(x_bin):
            if val != y_bin[key]:
                hemming_distance += 1

                    
        return hemming_distancegs