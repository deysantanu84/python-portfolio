# Given two binary strings A and B, count how many cyclic permutations of B when taken XOR with A give 0.
# NOTE: If there is a string, S0, S1, ... Sn-1 , then it's cyclic permutation is of the form
# Sk, Sk+1, ... Sn-1, S0, S1, ... Sk-1 where k can be any integer from 0 to N-1.
# 1 ≤ length(A) = length(B) ≤ 10^5
# First argument is a string A.
# Second argument is a string B.
# Return an integer denoting the required answer.
class Solution:
    def computeZUtil(self, string, Z):
        left = 0
        right = 0
        N = len(string)

        for i in range(1, N):
            if i > right:
                left = i
                right = i

                while right < N and string[right - left] == string[right]:
                    right += 1

                Z[i] = right - left
                right -= 1

            else:
                k = i - left
                if Z[k] < right - i + 1:
                    Z[i] = Z[k]

                else:
                    left = i

                    while right < N and string[right - left] == string[right]:
                        right += 1

                    Z[i] = right - left
                    right -= 1

    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        result = 0
        B += B
        B = B[0: len(B) - 1]
        string = A + "$" + B
        N = len(string)

        Z = [0 for _ in range(N)]
        self.computeZUtil(string, Z)

        for i in range(1, N):
            if Z[i] == len(A):
                result += 1

        return result


sol = Solution()
print(sol.solve("1001", "0011"))  # 1
print(sol.solve("111", "111"))  # 3
