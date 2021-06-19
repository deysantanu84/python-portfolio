# You are given a set of coins A.
# In how many ways can you make sum B assuming you have infinite amount of each coin in the set.
# NOTE:
# Coins in set A will be unique. Expected space complexity of this problem is O(B).
# The answer can overflow. So, return the answer % (10^6 + 7).
# 1 <= A <= 500
# 1 <= A[i] <= 1000
# 1 <= B <= 50000
# First argument is an integer array A representing the set.
# Second argument is an integer B.
# Return an integer denoting the number of ways.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):
        T = [0] * (B + 1)
        T[0] = 1

        for i in range(len(A)):
            j = A[i]
            while j <= B:
                T[j] += T[j - A[i]]
                j += 1

        return T[B] % (10**6 + 7)


sol = Solution()
print(sol.coinchange2([1, 2, 3], 4))  # 4
print(sol.coinchange2([10], 10))  # 1
print(sol.coinchange2([18, 24, 23, 10, 16, 19, 2, 9, 5, 12, 17, 3, 28, 29, 4, 13, 15, 8], 458))  # 867621
