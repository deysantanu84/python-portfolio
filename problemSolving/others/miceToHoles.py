# There are N mice and N holes that are places in a straight line. Each hole can accommodate only 1 mouse
# A denotes positions of mice, B denotes positions of holes
# A mouse can stay at his position, move one step right from x to x+1, or move one step left from x to x-1.
# Any of these moves consumes one minute
# Assign mice to holes so that the time when the last mouse gets inside a hole is minimized
# 1 <= N <= 10^5
# -10^9 <= A[i], B[i] <= 10^9
# Return an integer denoting the minimum time when the last mouse gets inside the holes
# A = [-4, 2, 3]
# B = [0, -2, 4]
# 2
# A = [-2]
# B = [-6]
# 4
class Solution:
    def __init__(self, micePositionList, holePositionList):
        self.micePositionList = micePositionList
        self.holePositionList = holePositionList

    # @param A: list of integers
    # @param B: list of integers
    # @return an integer
    def mice(self):
        minTime = 0

        return minTime


if __name__ == '__main__':
    A = [-4, 2, 3]
    B = [0, -2, 4]
    myObj = Solution(A, B)
    print(myObj.mice())
