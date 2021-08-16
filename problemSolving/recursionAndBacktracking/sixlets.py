# Given a array of integers A of size N and an integer B.
# Return number of non-empty subsequences of A of size B having sum <= 1000.
# 1 <= N <= 20
# 1 <= A[i] <= 1000
# 1 <= B <= N
# The first argument given is the integer array A.
# The second argument given is the integer B.
# Return number of subsequences of A of size B having sum <= 1000.
class Solution:
    def util(self, A, index, currSum, B, temp, result):
        if currSum < 0:
            return

        if B == 0:
            result.append(list(temp))
            return

        if index == len(A):
            return

        temp.append(A[index])
        self.util(A, index + 1, currSum - A[index], B - 1, temp, result)
        temp.pop()
        self.util(A, index + 1, currSum, B, temp, result)

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        result = []
        self.util(A, 0, 1000, B, [], result)
        return len(result)


sol = Solution()
print(sol.solve([1, 2, 8], 2))  # 3
print(sol.solve([5, 17, 1000, 11], 4))  # 0
print(sol.solve([123, 123, 123, 123, 123, 123, 123, 123, 123, 123], 4))  # 210
