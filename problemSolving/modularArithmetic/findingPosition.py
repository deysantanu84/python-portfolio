# Given an integer A which denotes the number of people standing in the queue.
# A selection process follows a rule where people standing on even positions are selected.
# Of the selected people a queue is formed and again out of these only people on even position are selected.
# This continues until we are left with one person.
# Find and return the position of that person in the original queue.
# 1 <= A <= 10^9
# The only argument given is integer A.
# Return the position of the last selected person in the original queue.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A & (A - 1) == 0:
            return A

        else:
            result = 1
            while A != 1:
                result <<= 1
                A >>= 1

            return result


sol = Solution()
print(sol.solve(10))  # 8
print(sol.solve(5))  # 4
