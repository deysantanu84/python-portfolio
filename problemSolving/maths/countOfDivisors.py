# Given an array of integers A, find and return the count of divisors of each element of the array.
# NOTE: Order of the resultant array should be same as the input array.
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 10^6
class Solution:
    countList = [2] * (10 ** 6 + 1)
    countList[1] = 1
    for i in range(2, (10**6 + 2)):
        for j in range(2 * i, (10 ** 6 + 1), i):
            countList[j] += 1

    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)
        result = [0] * N

        for i in range(N):
            result[i] = Solution.countList[A[i]]

        return result


sol = Solution()
print(sol.solve([2, 3, 4, 5]))  # [2, 2, 3, 2]
print(sol.solve([8, 9, 10]))  # [4, 3, 4]
print(sol.solve([3, 52, 66, 64, 14, 51, 6, 39, 5, 26, 80, 88, 60, 73, 67, 16, 1, 81, 62, 42, 83, 31, 40,
                 4, 32, 31, 44, 3, 20, 94, 93, 57, 2, 18, 32, 59, 91, 30, 45]))
# [2, 6, 8, 7, 4, 4, 4, 4, 2, 4, 10, 8, 12, 2, 2, 5, 1, 5, 4, 8, 2, 2, 8, 3, 6, 2, 6, 2, 6, 4, 4, 4, 2,
# 6, 6, 2, 4, 8, 6]
