# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
# Note:
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.

import operator

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common = dict()
        
        minimum_index = float('inf')
        
        # print('list2 is : ', list2)
        for index,elem in enumerate(list1):
            # print('elem is : ', elem)
            if elem in list2:
                index_sum = index + list2.index(elem)
                if index_sum < minimum_index:
                    minimum_index = index_sum
                common[elem] = index_sum
                
        result = []
        # print('minimum index is : ', minimum_index)
        for index, (elem, index_sum) in enumerate(common.items()):
            # print('elem is : ', elem, 'index is: ', index_sum)

            if index_sum == minimum_index:
                result.append(elem)
        return result
