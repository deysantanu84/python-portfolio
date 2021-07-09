# Given an integer A. Find and Return first positive A integers in ascending order containing
# only digits 1, 2 and 3.
# NOTE: All the A integers will fit in 32 bit integer.
# 1 <= A <= 29500
# The only argument given is integer A.
# Return an integer array denoting the first positive A integers in ascending order containing
# only digits 1, 2 and 3.
class Solution:
    def util(self, num):
        while num:
            temp = num % 10
            if temp == 1 or temp == 2 or temp == 3:
                num //= 10
                continue

            else:
                return False

        return True

    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        result = []
        i = 1

        while 1:
            if self.util(i):
                result.append(i)

            if len(result) == A or len(result) == 12:
                break

            i += 1

        temp = 3

        while A > len(result):
            N = len(result)

            for i in range(temp, N):
                for j in range(1, 4):
                    result.append(result[i] * 10 + j)
                    if len(result) == A:
                        break

                if len(result) == A:
                    break

            if len(result) == A:
                break

            temp = N

        return result


sol = Solution()
print(sol.solve(3))  # [1, 2, 3]
print(sol.solve(7))  # [1, 2, 3, 11, 12, 13, 21]
