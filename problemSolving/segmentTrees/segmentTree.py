# Given an array A of size N and Q queries. Perform following queries:
# 1 V 0 append V in the back of array.
# 2 X V set A[X] = V.
# 3 X 0 delete A[X]. Note: All element at back of X move forward to occupy void.
# 4 X Y find sum in range [X, Y].
# NOTE: For the query of type 4 X Y, output the sum % 10^9 + 7.
# 1 <= N,Q <= 100000
# 1 <= A[i],V <=100000
# 1 <= X,Y <= N' Where, N' is current size of array.
# First argument contains an integer array A.
# Second argument contains a Q x 3 Matrix B.
# Return an integer array containing answer to all query of type 4 X Y in chronological order.
# TLE
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
                tree[position] = tree[2 * position + 1] + tree[2 * position + 2]

        build(0, N - 1, 0)
        return tree

    @staticmethod
    def rangeQuery(tree, A, queryLeft, queryRight):
        N = len(A)

        def query(qL, qR, start, end, position):
            if qL <= start and qR >= end:
                return tree[position]

            if qL > end or qR < start:
                return 0

            mid = (start + end) // 2
            return (query(qL, qR, start, mid, 2 * position + 1) + query(qL, qR, mid + 1, end, 2 * position + 2)) \
                % (10 ** 9 + 7)

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
                tree[position] = tree[2 * position + 1] + tree[2 * position + 2]

        update(idx, value, 0, N - 1, 0)

    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        result = []
        tree = self.buildTree(A)

        for i in range(len(B)):
            if B[i][0] == 4:
                result.append(self.rangeQuery(tree, A, B[i][1] - 1, B[i][2] - 1))

            elif B[i][0] == 1:
                A.append(B[i][1])
                tree = self.buildTree(A)

            elif B[i][0] == 3:
                A.pop(B[i][1] - 1)
                if len(A):
                    tree = self.buildTree(A)

            else:
                self.updateQuery(tree, A, B[i][1] - 1, B[i][2])

        return result


sol = Solution()
print(sol.solve([1, 2, 5, 3, 4], [[4, 2, 4], [3, 3, 0], [1, 6, 0], [4, 3, 5]]))  # [10, 13]
