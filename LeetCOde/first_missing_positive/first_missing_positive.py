# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.



class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # print('type of nums is : ', type(nums))
        dedupedlist = list(set(nums))
        print('dedupedlist  is : ', dedupedlist)

        dedupedlist.sort()
        print('sorted dedupedlist is : ',dedupedlist)
        expected_integer = 1

        # print nums

        for integer in dedupedlist:
        	if integer > 0:
        		print('int is : ', integer)
        		if integer == expected_integer:
        			expected_integer = expected_integer + 1 
        			print('next expected int is : ', expected_integer)
        		else:
        			return expected_integer
        return expected_integer


if __name__ == '__main__':
	mysolx = Solution()
	firstmissingint = mysolx.firstMissingPositive([3,4,-1,1])
	print('firstmissingint is : ', firstmissingint)