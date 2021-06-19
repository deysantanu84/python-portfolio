# Find out the number of A digit positive numbers, whose digits on being added equals to a given number B.
# Note that a valid number starts from digits 1-9 except the number 0 itself.
# i.e. leading zeroes are not allowed.
# Since the answer can be large, output answer modulo 1000000007
# 1 <= A <= 1000
# 1 <= B <= 10000
# First argument is the integer A
# Second argument is the integer B
# Return a single integer, the answer to the problem
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        resultGrid = [[0] * (B + 1) for _ in range(A + 1)]
        resultGrid[0][0] = 1

        for i in range(A):
            for j in range(B):
                for digit in range(10):
                    if j + digit <= B:
                        resultGrid[i + 1][j + digit] += resultGrid[i][j]
                    else:
                        break

        return resultGrid[A][B] % 1000000007


sol = Solution()
print(sol.solve(2, 4))  # 4
print(sol.solve(1, 3))  # 1
