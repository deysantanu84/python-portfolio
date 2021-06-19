# There are N Mice and N holes that are placed in a straight line.
# Each hole can accommodate only 1 mouse.
# The positions of Mice are denoted by array A and the position of holes are denoted by array B.
# A mouse can stay at his position, move one step right from x to x + 1,
# or move one step left from x to x − 1. Any of these moves consumes 1 minute.
# Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.
# 1 <= N <= 10^5
# -109 <= A[i], B[i] <= 10^9
# First argument is an integer array A.
# Second argument is an integer array B.
# Return an integer denoting the minimum time when the last mouse gets inside the holes.
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def mice(self, A, B):
		result = 0
		N = len(A)
		M = len(B)

		if N != M:
			return -1

		A.sort()
		B.sort()

		for index in range(N):
			if result < abs(A[index] - B[index]):
				result = abs(A[index] - B[index])

		return result


sol = Solution()
print(sol.mice([-4, 2, 3], [0, -2, 4]))  # 2
print(sol.mice([-2], [-6]))  # 4
