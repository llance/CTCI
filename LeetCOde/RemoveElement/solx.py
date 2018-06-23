class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for value in nums[:]:
            if value == val:
                nums.remove(value)
        print(nums)
        return len(nums)
                