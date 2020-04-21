# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        size = binaryMatrix.dimensions()
        rows = size[0]
        columns = size[1]
        mini = float('inf')
        i = 0 
        found = -1
        while i < rows:
            left  = 0 
            right = size[1]
            mid = -1
            while left  < right:
                mid = (left + (right - 1))/2
                if binaryMatrix.get(i,mid) == 1:
                    right = mid
                    found = mid
                else:
                    left = mid + 1
            if found != -1: 
                mini = min(mini, found)
            i += 1
        if mini ==  float('inf'):
            return -1
        return mini
---------------------------------------------------------------------------------------
class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        size = binaryMatrix.dimensions()
        rows = size[0]
        columns = size[1]
        found = 0 
        i = size[0]
        j = columns -1
        while i > rows and j >= 0 :
            print(i, j)
            x = binaryMatrix.get(i, j)
            print(x)
            if x == 0:
                j += 1
            else:
                found = i
                i -= 1
        return found 