class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = nums1 + nums2
        print(merged_array)
        
        array_len = len(merged_array)
        
        merged_array_sorted = sorted(merged_array)
        print(merged_array_sorted)
        if len(merged_array_sorted) % 2 == 0 :
            print(int(array_len/2))
            return (merged_array_sorted[int(array_len/2) -1] + merged_array_sorted[int(array_len/2) ])/2
        else:
            return merged_array_sorted[int((len(merged_array_sorted)+1)/2)-1 ]