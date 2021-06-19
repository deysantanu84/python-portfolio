# As it is Tushar's Birthday on March 1st, he decided to throw a party to all his friends at
# TGI Fridays in Pune. Given are the eating capacity of each friend, filling capacity of each
# dish and cost of each dish. A friend is satisfied if the sum of the filling capacity of dishes
# he ate is equal to his capacity. Find the minimum cost such that all of Tushar's friends are
# satisfied (reached their eating capacity).
# NOTE:
# Each dish is supposed to be eaten by only one person. Sharing is not allowed.
# Each friend can take any dish unlimited number of times.
# There always exists a dish with filling capacity 1 so that a solution always exists.
# |A| <= 1000
# |B| <= 1000
# |C| <= 1000
# First Argument is vector A, denoting eating capacities
# Second Argument is vector B, denoting filling capacities
# Third Argument is vector C, denoting cost
# Return a single integer, the answer to the problem
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, A, B, C):
        result = 0
        P = max(A) + 1
        Q = len(B) + 1

        resultGrid = [[i and float('inf') or 0] * Q for i in range(P)]

        for i in range(P):
            for j in range(1, Q):
                if i - B[j - 1] >= 0:
                    resultGrid[i][j] = min(resultGrid[i][j - 1],
                                           resultGrid[i - B[j - 1]][j] + C[j - 1])

                else:
                    resultGrid[i][j] = resultGrid[i][j - 1]

        for entry in A:
            result += resultGrid[entry][-1]

        return result


sol = Solution()
print(sol.solve([2, 4, 6], [2, 1, 3], [2, 5, 3]))  # 12
print(sol.solve([2], [1], [2]))  # 4
