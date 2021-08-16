# Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.
# Since the answer may be large, return the answer modulo (10^9 + 7).
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 10^9
# 1 <= B <= 10^6
# The first argument given is the integer array A.
# The second argument given is the integer B.
# Return the total number of pairs for which the sum is divisible by B modulo (109 + 7).
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in range(len(A)):
            A[i] = A[i] % B

        result = 0
        frequency = {}

        for i in range(len(A)):
            if A[i] == 0:
                if 0 in frequency.keys():
                    result = (result + frequency[0]) % (10**9 + 7)

            if (B - A[i]) in frequency.keys():
                result = (result + frequency[B - A[i]]) % (10**9 + 7)

            if A[i] in frequency.keys():
                frequency[A[i]] += 1
            else:
                frequency[A[i]] = 1

        return result % (10**9 + 7)


sol = Solution()
print(sol.solve([1, 2, 3, 4, 5], 2))  # 4
print(sol.solve([5, 17, 100, 11], 28))  # 1
