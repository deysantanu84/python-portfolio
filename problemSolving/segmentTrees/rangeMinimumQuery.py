# Given an integer array A of size N.
# You have to perform two types of query, in each query you are given three integers x,y,z.
# If x = 0, then update A[y] = z.
# If x = 1, then output the minimum element in the array A between index y and z inclusive.
# Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.
# 1 <= N, M <= 10^5
# 1 <= A[i] <= 10^9
# If x = 0, 1<= y <= N and 1 <= z <= 10^9
# If x = 1, 1<= y <= z <= N
# First argument is an integer array A of size N.
# Second argument is a 2-D array B of size M x 3 denoting queries.
# Return an integer array denoting the output of each query where value of x is 1.
class Solution:
    @staticmethod
    def buildTree(A):
        N = len(A)
        tree = [-1 for _ in range(4 * N)]

        def build(start, end, position):
            if start == end:
                tree[position] = A[start]

            else:
                mid = (start + end) // 2
                build(start, mid, 2 * position + 1)
                build(mid + 1, end, 2 * position + 2)
                tree[position] = min(tree[2 * position + 1], tree[2 * position + 2])

        build(0, N - 1, 0)
        return tree

    @staticmethod
    def rangeQuery(tree, A, queryLeft, queryRight):
        N = len(A)

        def query(qL, qR, start, end, position):
            if qL <= start and qR >= end:
                return tree[position]

            if qL > end or qR < start:
                return float('inf')

            mid = (start + end) // 2
            return min(query(qL, qR, start, mid, 2 * position + 1),
                       query(qL, qR, mid + 1, end, 2 * position + 2))

        return query(queryLeft, queryRight, 0, N - 1, 0)

    @staticmethod
    def updateQuery(tree, A, idx, value):
        N = len(A)

        def update(index, val, start, end, position):
            if start == end:
                A[index] = val
                tree[position] = val
            else:
                mid = (start + end) // 2
                if start <= index <= mid:
                    update(index, val, start, mid, 2 * position + 1)
                else:
                    update(index, val, mid + 1, end, 2 * position + 2)
                tree[position] = min(tree[2 * position + 1], tree[2 * position + 2])

        update(idx, value, 0, N - 1, 0)

    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        result = []
        tree = self.buildTree(A)

        for i in range(len(B)):
            if B[i][0]:
                result.append(self.rangeQuery(tree, A, B[i][1] - 1, B[i][2] - 1))
            else:
                self.updateQuery(tree, A, B[i][1] - 1, B[i][2])

        return result


sol = Solution()
print(sol.solve([1, 4, 1], [[1, 1, 3], [0, 1, 5], [1, 1, 2]]))  # [1, 4]
print(sol.solve([5, 4, 5, 7], [[1, 2, 4], [0, 1, 2], [1, 1, 4]]))  # [4, 2]
print(sol.solve([18, 10, 1, 20, 25, 4, 9, 13, 15, 6, 21, 7], [[1, 8, 12], [0, 4, 7], [1, 1, 3], [1, 5, 11],
                                                              [1, 3, 9], [1, 7, 12], [1, 7, 10], [0, 12, 20]]))
# [6, 1, 4, 1, 6, 6]
