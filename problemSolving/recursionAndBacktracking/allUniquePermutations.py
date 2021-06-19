# Given an array A of size N denoting collection of numbers that might contain duplicates,
# return all possible unique permutations.
# NOTE: No 2 entries in the permutation sequence should be the same.
# WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.
# Example : next_permutations in C++ / itertools.permutations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points.
# 1 <= |A| <= 9
from collections import Counter


class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):
		res = []

		def dfs(counter, path):
			if len(path) == len(A):
				res.append(path)
				return
			for x in counter:
				if counter[x]:
					counter[x] -= 1
					dfs(counter, path+[x])
					counter[x] += 1
		dfs(Counter(A), [])
		return res


obj = Solution()
print(obj.permute([1, 1, 2]))  # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
print(obj.permute([1, 2]))  # [[1, 2], [2, 1]]
print(obj.permute([1, 2, 3, 4, 5, 6, 7, 8]))
print(obj.permute([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
