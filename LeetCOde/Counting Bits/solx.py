class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits_list = []
        for integer in range(num+1):
            int_bin_fmt = str('{0:032b}'.format(integer))
            # print('int_bin_fmt is : ', int_bin_fmt)
            
            bits_list.append(int_bin_fmt.count('1'))
            
        # print('bits_list is : ', bits_list)
        return bits_list