# You are given a string A consisting of 1's and 0's. Now the task is to make the string consisting
# of only 1's. But you are allowed to perform only the following operation:
# Take exactly B consecutive elements of string and change 1 to 0 and 0 to 1.
# Each operation takes 1 unit time so you have to determine the minimum time required to
# make the string of 1's only. If not possible return -1.
# 2 ≤ length of A ≤ 10^5
# 2 ≤ B ≤ (length of A)
# First argument is a string A consisting if 1's and 0's.
# Second argument is an integer B which represents the number of consecutive elements which can be changed.
# Return an integer which is the minimum time to make the string of 1's only or -1 if not possible.
# TLE
class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        A = list(A)
        result = 0

        for i in range(N):
            if A[i] == '0':
                for j in range(i, i + B):
                    if j >= N:
                        return -1

                    if A[j] == '1':
                        A[j] = '0'
                    else:
                        A[j] = '1'

                result += 1

        return result


sol = Solution()
print(sol.solve("00010110", 3))  # 3
print(sol.solve("011", 3))  # -1
