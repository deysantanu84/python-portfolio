# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
# 1 <= N <= 10^5
# -10^9 <= A[i] <= 10^9
# First and only argument is an integer array A representing the rating of children.
# Return an integer, representing the minimum candies to be given.
class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        up = 1
        down = 0
        result = 1
        peak = 0

        for index in range(1, len(A)):
            if A[index - 1] < A[index]:
                up += 1
                down = 0
                result += up
                peak = up

            elif A[index - 1] == A[index]:
                down = 0
                peak = 0
                up = 1
                result += 1

            else:
                down += 1
                up = 1
                result += down
                if peak <= down:
                    result += 1

        return result


sol = Solution()
print(sol.candy([1, 2]))  # 3
print(sol.candy([1, 5, 2, 1]))  # 7
