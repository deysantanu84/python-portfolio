# Given a Tree of A nodes having A-1 edges. Each node is numbered from 1 to A where 1 is the root of the tree.
# You are given Q queries. In each query, you will be given two integers L and X.
# Find the value of such node which lies at level L mod (MaxDepth + 1) and has value greater than or equal to X.
# Answer to the query is the smallest possible value or -1,
# if all the values at the required level are smaller than X.
# NOTE:
# Level and Depth of the root is considered as 0.
# It is guaranteed that each edge will be connecting exactly two different nodes of the tree.
# Please read the input format for more clarification.
# 2 <= A, Q(size of array E and F) <= 10^5
# 1 <= B[i], C[i] <= A
# 1 <= D[i], E[i], F[i] <= 10^6
# The first argument is an integer A denoting the number of nodes.
# The second and third arguments are the integer arrays B and C where for each i (0 <= i < A-1),
# B[i] and C[i] are the nodes connected by an edge.
# The fourth argument is an integer array D, where D[i] denotes the value of the (i+1)th node
# The fifth and sixth arguments are the integer arrays E and F where
# for each i (0 <= i < Q), E[i] denotes L and F[i] denotes X for ith query.
# Return an array of integers where the ith element denotes the answer to ith query.
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F):
        pass


sol = Solution()
print(sol.solve(5, [1, 4, 3, 1], [5, 2, 4, 4], [7, 38, 27, 37, 1], [1, 1, 2], [32, 18, 26]))  # [37, 37, 27]
print(sol.solve(3, [1, 2], [3, 1], [7, 15, 27], [1, 10, 1], [29, 6, 26]))  # [-1, 7, 27]
