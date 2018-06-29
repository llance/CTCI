class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top_view_skyline = [0] * len(grid)
        left_view_skyline = [0] * len(grid)
        
        for i in range(len(grid)):
            # print(grid[i])
            left_view_skyline[i] = max(grid[i])
            
            for j in range(len(grid[i])):
                if grid[i][j] > top_view_skyline[j]:
                    top_view_skyline[j] = grid[i][j]
            
        print(left_view_skyline)
        print(top_view_skyline)
        
# [3, 0, 8, 4], 
# [2, 4, 5, 7],
# [9, 2, 6, 3],
# [0, 3, 1, 0] 



# [8, 4, 8, 7],
# [7, 4, 7, 7],
# [9, 4, 8, 7],
# [3, 3, 3, 3] 

# top [9, 4, 8, 7]

# left[8, 7, 9, 3]
        total_increase = 0
        for i in range(len(grid)):            
            for j in range(len(grid[i])):
                # print(grid[i][j])
                if top_view_skyline[j] > left_view_skyline[i]:
                    # grid[i][j] = left_view_skyline[i]
                    total_increase = total_increase + (left_view_skyline[i] - grid[i][j])
                else:
                    # grid[i][j] = top_view_skyline[j]
                    total_increase = total_increase + (top_view_skyline[j] - grid[i][j])
                    
        print(total_increase)
        return total_increase