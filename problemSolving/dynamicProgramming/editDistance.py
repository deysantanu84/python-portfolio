# Given two strings A and B, find the minimum number of steps required to convert A to B.
# (each operation is counted as 1 step.)
# You have the following 3 operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character
# 1 <= length(A), length(B) <= 450
# The first argument of input contains a string, A.
# The second argument of input contains a string, B.
# Return an integer, representing the minimum number of steps required.
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        distanceMatrix = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

        for i in range(len(A) + 1):
            distanceMatrix[i][0] = i

            for j in range(1, len(B)+1):
                if i == 0:
                    distanceMatrix[0][j] = j

                elif A[i - 1] == B[j - 1]:
                    distanceMatrix[i][j] = distanceMatrix[i - 1][j - 1]

                else:
                    distanceMatrix[i][j] = min(distanceMatrix[i - 1][j - 1],  # replace
                                               distanceMatrix[i - 1][j],  # delete
                                               distanceMatrix[i][j - 1]) + 1  # insert

        return distanceMatrix[-1][-1]


sol = Solution()
print(sol.minDistance("abad", "abac"))  # 1
print(sol.minDistance("Anshuman", "Antihuman"))  # 2
