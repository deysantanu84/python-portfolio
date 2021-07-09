# Bob has an array A of N integers. Initially, all the elements of the array are zero.
# Bob asks you to perform Q operations on this array.
# You have to perform three types of query, in each query you are given three integers x, y and z.
# if x = 1: Update the value of A[y] to 2 * A[y] + 1.
# if x = 2: Update the value A[y] to ⌊A[y]/2⌋ , where ⌊⌋ is Greatest Integer Function.
# if x = 3: Take all the A[i] such that y <= i <= z and convert them into their corresponding binary strings.
# Now concatenate all the binary strings and find the total no. of '1' in the resulting string.
# Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y,
# B[i][2] denotes z.
# 1 <= N, Q <= 100000
# 1 <= y, z <= N
# 1 <= x <= 3
# The first argument has the integer A.
# The second argument is a 2d matrix B, of size Q x 3, representing the queries.
# Return an array of integers where ith index represents the answer of the ith type 3 query.
N = 100003
a = [0 for _ in range(N)]
tree = [0 for _ in range(4 * N)]


class Solution:
    def update1(self, n, st, en, x):
        if st == en:
            a[x] += 1
            tree[n] += 1

        else:
            mid = (st + en) // 2
            if st <= x <= mid:
                self.update1(2 * n, st, mid, x)
            else:
                self.update1(2 * n + 1, mid + 1, en, x)

            tree[n] = tree[2 * n] + tree[2 * n + 1]

    def update2(self, n, st, en, x):
        if st == en:
            if a[x] == 0:
                return
            a[x] -= 1
            tree[n] -= 1

        else:
            mid = (st + en) // 2
            if st <= x <= mid:
                self.update2(2 * n, st, mid, x)
            else:
                self.update2(2 * n + 1, mid + 1, en, x)

            tree[n] = tree[2 * n] + tree[2 * n + 1]

    def query(self, n, st, en, left, right):
        if right < st or en < left:
            return 0

        if left <= st and en <= right:
            return tree[n]

        mid = (st + en) // 2
        return self.query(2 * n, st, mid, left, right) + self.query(2 * n + 1, mid + 1, en, left, right)

    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        global N, a, tree
        result = []
        N = 100003
        a = [0 for _ in range(N)]
        tree = [0 for _ in range(4 * N)]

        for query in B:
            if query[0] == 1:
                self.update1(1, 1, A, query[1])

            elif query[0] == 2:
                self.update2(1, 1, A, query[1])

            else:
                result.append(self.query(1, 1, A, query[1], query[2]))

        return result


sol = Solution()
print(sol.solve(5, [[1, 1, -1], [1, 2, -1], [1, 3, -1], [3, 1, 3], [3, 2, 4]]))  # [3, 2]
print(sol.solve(5, [[1, 1, -1], [1, 2, -1], [3, 1, 3], [2, 1, -1], [3, 1, 3]]))  # [2, 1]
