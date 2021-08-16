# Given an integer A denoting the size of the array consisting all ones.
# You are given Q queries, for each query there are two integer x and y:
# If x is 0, then update the value of array at index y to 0.
# If x is 1, then output the index of yth one in the array. If there is no such index then output -1.
# NOTE 1: There will atleast 1 query where value of x is 1.
# 1 <= A, Q <= 10^5
# 0 <= x <= 1
# 1 <= y <= A
# First argument is an integer A denoting the size of array.
# Second argument is a 2-D array B of size Q x 2 where B[i][0] denotes x and B[i][1] denotes y.
# Return an integer array denoting the output of each query where x is 1.
from math import ceil, log


class Solution:
    def buildTree(self, index, start, end, tree):
        if start == end:
            tree[index] = 1
        else:
            mid = (start + end) // 2
            leftChild = 2 * index + 1
            rightChild = 2 * index + 2
            self.buildTree(leftChild, start, mid, tree)
            self.buildTree(rightChild, mid + 1, end, tree)
            tree[index] = tree[leftChild] + tree[rightChild]

    def query(self, index, start, end, val, tree):
        if start == end:
            return start + 1

        mid = (start + end) // 2
        leftChild = 2 * index + 1
        rightChild = 2 * index + 2
        if tree[leftChild] >= val:
            return self.query(leftChild, start, mid, val, tree)
        else:
            return self.query(rightChild, mid + 1, end, val - tree[leftChild], tree)

    def update(self, index, start, end, val, tree):
        if start > val or val > end:
            return

        if start == end:
            tree[index] = 0
        else:
            mid = (start + end) // 2
            leftChild = 2 * index + 1
            rightChild = 2 * index + 2
            self.update(leftChild, start, mid, val, tree)
            self.update(rightChild, mid + 1, end, val, tree)
            tree[index] = tree[leftChild] + tree[rightChild]

    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        result = []
        x = ceil(log(A) / log(2))
        x = pow(2, x + 1) - 1
        tree = [0 for _ in range(x)]

        self.buildTree(0, 0, A - 1, tree)

        for i in range(len(B)):
            if B[i][0] == 1:
                if B[i][1] > tree[0]:
                    result.append(-1)
                else:
                    result.append(self.query(0, 0, A - 1, B[i][1], tree))
            elif B[i][0] == 0:
                self.update(0, 0, A - 1, B[i][1] - 1, tree)

        return result


sol = Solution()
print(sol.solve(4, [[1, 2], [0, 2], [1, 4]]))  # [2, -1]
print(sol.solve(5, [[0, 3], [1, 4], [0, 3], [1, 5]]))  # [5, -1]
