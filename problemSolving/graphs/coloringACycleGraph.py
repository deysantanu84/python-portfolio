# Given the number of vertices A in a Cyclic Graph.
# Your task is to determine the number of colors required to color the graph so that
# no two Adjacent vertices have the same color.
# 3 <= A <= 10^9
# First argument is an integer A denoting the number of vertices in the Cyclic Graph.
# Return an single integer denoting the number of colors required to color the graph so that
# no two Adjacent vertices have the same color.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if not A % 2:
            return 2
        else:
            return 3


sol = Solution()
print(sol.solve(5))  # 3
print(sol.solve(4))  # 2
