class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size_of_array = len(nums)
        
        unique_nums = set(nums)
        
        all_nums_within_range = list(range(1, size_of_array+1))
        
        dissapeared_number = list(set(all_nums_within_range) - unique_nums)

        
        return dissapeared_number
        