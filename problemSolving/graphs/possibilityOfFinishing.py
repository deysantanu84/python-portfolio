# There are a total of A courses you have to take, labeled from 1 to A.
# Some courses may have prerequisites, for example to take course 2 you have to first take course 1,
# which is expressed as a pair: [1,2].
# So you are given two integer array B and C of same size where for each i (B[i], C[i]) denotes a pair.
# Given the total number of courses and a list of prerequisite pairs,
# is it possible for you to finish all courses?
# Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.
# 1 <= A <= 6*10^4
# 1 <= length(B) = length(C) <= 10^5
# 1 <= B[i], C[i] <= A
# The first argument of input contains an integer A, representing the number of courses.
# The second argument of input contains an integer array, B.
# The third argument of input contains an integer array, C.
# Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        result = 0
        queue = []
        paths = [[] for _ in range(A)]
        temp = [0] * A

        for i, j in zip(B, C):
            paths[j - 1].append(i - 1)
            temp[i - 1] += 1

        for i in range(A):
            if not temp[i]:
                queue.append(i)

        while queue:
            curr = queue.pop(0)
            result += 1

            for j in paths[curr]:
                temp[j] -= 1
                if not temp[j]:
                    queue.append(j)

        if result == A:
            return 1

        return 0


sol = Solution()
print(sol.solve(3, [1, 2], [2, 3]))  # 1
print(sol.solve(2, [1, 2], [2, 1]))  # 0
