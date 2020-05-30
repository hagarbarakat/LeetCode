class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l1 = []
        for i in range(numRows):
            rows = [None for _ in range(i+1)]
            rows[0], rows[-1] = 1, 1 # first and last poistions 
            
            for j in range(1, len(rows)-1):
                rows[j] = l1[i - 1][j - 1] + l1[i - 1][j]
            l1.append(rows)
        return l1