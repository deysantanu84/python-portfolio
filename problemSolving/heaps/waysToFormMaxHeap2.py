# Max heap is a special kind of complete binary tree in which for every node the value present
# in that node is greater than the value present in it’s children nodes.
# Given an array A of size N consisting of N - 1 distinct elements. In other words there is
# exactly one element that is repeated.
# It is given that the element that would repeat would be either the maximum element or the minimum element.
# Find the number of structurally different Max heaps possible using all the N elements of the array
# i.e. Max heap of size N.
# As final answer can be very large return your answer modulo 10^9 + 7.
# 1 <= N <= 1000
# First and only argument is an integer array A.
# Return an integer denoting the number of structurally different Max heaps possible modulo 10^9 + 7.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        pass


sol = Solution()
print(sol.solve([1, 5, 5]))  # 2
print(sol.solve([2, 2, 7]))  # 1
