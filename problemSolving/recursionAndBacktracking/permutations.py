# Given an integer array A of size N denoting collection of numbers,
# return all possible permutations.
# NOTE:
# No two entries in the permutation sequence should be the same.
# For the purpose of this problem, assume that all the numbers in the collection are unique.
# WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.
# Example : next_permutations in C++ / itertools.permutations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points.
# 1 <= N <= 9
from collections import Counter


class Solution:
    def permute(self, A):
        result = []

        def dfs(counter, path):
            if len(path) == len(A):
                result.append(path)
                return

            for x in counter:
                if counter[x]:
                    counter[x] -= 1
                    dfs(counter, path+[x])
                    counter[x] += 1

        dfs(Counter(A), [])
        return result


obj = Solution()
print(obj.permute([1, 2, 3]))
