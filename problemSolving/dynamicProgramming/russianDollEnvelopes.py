# Given a matrix of integers A of size N x 2 describing dimensions of N envelopes,
# where A[i][0] denotes the height of the ith envelope and A[i][1] denotes the width of the ith envelope.
# One envelope can fit into another if and only if both the width and height of one envelope
# is greater than the width and height of the other envelope.
# Find the maximum number of envelopes you can put one inside other.
# 1 <= N <= 1000
# 1 <= A[i][0], A[i][1] <= 10^9
# The only argument given is the integer matrix A.
# Return an integer denoting the maximum number of envelopes you can put one inside other.
class Solution:
    def util(self, A):
        temp = [1] * len(A)
        result = 1

        for index in range(1, len(A)):
            for index1 in range(0, index):
                if A[index1][1] < A[index][1] and temp[index] < temp[index1]+1:
                    temp[index] = temp[index1] + 1

            if result < temp[index]:
                result = temp[index]

        return result

    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A, key=lambda entry: (entry[0], -1 * entry[1]))
        return self.util(A)


sol = Solution()
print(sol.solve([[5, 4], [6, 4], [6, 7], [2, 3]]))  # 3
print(sol.solve([[8, 9], [8, 18]]))  # 1
