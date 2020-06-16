class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
            if A[0] <= A[-1]:
                A = A[::-1] # reverse array
            for i in range(1,len(A)):
                if A[i-1] < A[i]:
                    return False
            return True