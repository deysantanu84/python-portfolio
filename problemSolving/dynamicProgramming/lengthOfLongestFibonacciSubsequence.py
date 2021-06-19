# Given a strictly increasing array A of positive integers forming a sequence.
# A sequence X1, X2, X3, ..., XN is fibonacci like if
# N > =3
# Xi + Xi+1 = Xi+2 for all i+2 <= N
# Find and return the length of the longest Fibonacci-like subsequence of A.
# If one does not exist, return 0.
# NOTE: A subsequence is derived from another sequence A by deleting any number of elements
# (including none) from A, without changing the order of the remaining elements.
# 3 <= length of the array <= 1000
# 1 <= A[i] <= 10^9
# The only argument given is the integer array A.
# Return the length of the longest Fibonacci-like subsequence of A.
# If one does not exist, return 0.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        result = 0
        N = len(A)
        indexDict = {}

        for index, entry in enumerate(A):
            indexDict[entry] = index

        resultGrid = [[2 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(i):
                temp = A[i] - A[j]

                if temp in indexDict and temp < A[j]:
                    resultGrid[i][j] = resultGrid[j][indexDict[temp]] + 1
                    result = max(result, resultGrid[i][j])

        if result >= 3:
            return result
        else:
            return 0


sol = Solution()
print(sol.solve([1, 2, 3, 4, 5, 6, 7, 8]))  # 5
print(sol.solve([1, 3, 7, 11, 12, 14, 18]))  # 3
