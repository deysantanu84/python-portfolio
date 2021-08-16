# Given a binary string A of size N and an integer matrix B of size Q x 3.
# Matrix B has Q queries:
# For queries of type B[i][0] = 1, flip the value at index B[i][1] in A if and only if the value at that index
# is 0 and return -1.
# For queries of type B[i][0] = 0, Return the value of the binary string from index B[i][1] to B[i][2] modulo 3.
# Note: Rows are numbered from top to bottom and columns are numbered from left to right.
# 1 <= N <= 100000
# 1 <= Q <= 200000
# 1 <= B[i][1], B[i][2] <= N
# B[i][1] <= B[i][2]
# The first argument given is the string A.
# The second argument given is the integer matrix B of size Q * 3.
# Return an array of size Q where ith value is answer to ith query.
from math import ceil, log


class Solution:
    def buildTree(self, index, start, end, A, tree):
        if start == end:
            tree[index] = ord(A[start]) - ord('0')
        else:
            mid = (start + end) // 2
            leftChild = 2 * index + 1
            rightChild = 2 * index + 2
            self.buildTree(leftChild, start, mid, A, tree)
            self.buildTree(rightChild, mid + 1, end, A, tree)

            if (end - mid) % 2 == 0:
                if tree[leftChild] == 1:
                    temp = 1
                elif tree[leftChild] == 2:
                    temp = 2
                else:
                    temp = 0
            else:
                if tree[leftChild] == 1:
                    temp = 2
                elif tree[leftChild] == 2:
                    temp = 1
                else:
                    temp = 0

            tree[index] = (temp + tree[rightChild]) % 3

    def query(self, index, start, end, left, right, res, tree):
        self.res = res
        if left > end or start > right:
            return

        if left <= start and end <= right:
            if (end - start + 1) % 2 == 0:
                if self.res == 1:
                    temp = 1
                elif self.res == 2:
                    temp = 2
                else:
                    temp = 0
            else:
                if self.res == 1:
                    temp = 2
                elif self.res == 2:
                    temp = 1
                else:
                    temp = 0

            self.res = (temp + tree[index]) % 3
            return self.res

        mid = (start + end) // 2
        leftChild = 2 * index + 1
        rightChild = 2 * index + 2
        self.query(leftChild, start, mid, left, right, self.res, tree)
        self.query(rightChild, mid + 1, end, left, right, self.res, tree)
        return self.res

    def update(self, index, start, end, val, tree):
        if start > val or val > end:
            return

        if start == end:
            if tree[index] == 0:
                tree[index] = 1
        else:
            mid = (start + end) // 2
            leftChild = 2 * index + 1
            rightChild = 2 * index + 2
            self.update(leftChild, start, mid, val, tree)
            self.update(rightChild, mid + 1, end, val, tree)

            if (end - mid) % 2 == 0:
                if tree[leftChild] == 1:
                    temp = 1
                elif tree[leftChild] == 2:
                    temp = 2
                else:
                    temp = 0
            else:
                if tree[leftChild] == 1:
                    temp = 2
                elif tree[leftChild] == 2:
                    temp = 1
                else:
                    temp = 0

            tree[index] = (temp + tree[rightChild]) % 3

    # @param A : string
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        result = []
        A = str(A)
        N = len(A)
        x = ceil(log(N) / log(2))
        x = pow(2, x + 1) - 1
        tree = [0 for _ in range(x)]

        self.buildTree(0, 0, N - 1, A, tree)

        for i in range(len(B)):
            if B[i][0] == 0:
                res = self.query(0, 0, N - 1, B[i][1] - 1, B[i][2] - 1, 0, tree)
                result.append(res)
            elif B[i][0] == 1:
                self.update(0, 0, N - 1, B[i][1] - 1, tree)
                result.append(-1)

        return result


sol = Solution()
print(sol.solve(10010, [[0, 3, 5], [0, 3, 4], [1, 2, -1], [0, 1, 5]]))  # [2, 1, -1, 2]
# For query 1, binary string from index 3 to 5 is 010 = 2. So 2 mod 3 = 2.
# For query 2, binary string from index 3 to 4 is 01 = 1. So 1 mod 3 = 1.
# After query 3, given string changes to 11010.
# For query 4, binary string from index 1 to 5 is 11010 = 26. So 26 mod 3 = 2.
# So, output array is [2, 1, -1, 2].

print(sol.solve(11111, [[0, 2, 4], [1, 2, -1], [0, 2, 4]]))  # [1, -1, 1]
# For query 1, binary string from index 2 to 4 is 111 = 7. So 7 od 3 = 1.
# After query 2, string remains same as there is already 1 at index 2.
# For query 3, binary string from index 2 to 4 is 111 = 7. So 7 od 3 = 1.
# So, output array is [1, -1, 1].
