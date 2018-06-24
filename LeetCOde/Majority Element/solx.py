class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        
        major_threshold = int(len(nums)/2 )
        print("major_threshold is : ", major_threshold)
        count = Counter(nums)
        
        print(count)
        
        for key, val in enumerate(count):
            print("key is :",  key, "val is : ", count[val])
            if count[val] > major_threshold:
                return val