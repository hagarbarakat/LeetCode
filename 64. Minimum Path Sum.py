class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i = len(grid)-1
        j = len(grid[0])-1
        while i >= 0:
            j = len(grid[0])-1
            while j >= 0:
                if i == len(grid)-1 and j != len(grid[0])-1:
                    grid[i][j] = grid[i][j] +  grid[i][j + 1]
                    print(grid[i][j])
                elif j == len(grid[0])-1 and i != len(grid) -1:
                    grid[i][j] = grid[i][j] + grid[i + 1][j]
                    print(grid[i][j])
                elif  j !=len(grid[0])-1  and i !=len(grid) - 1:
                    grid[i][j] = grid[i][j] + min(grid[i + 1][j],grid[i][j + 1])
                    print(grid[i][j])
                j -= 1
            i -= 1 
        return grid[0][0]