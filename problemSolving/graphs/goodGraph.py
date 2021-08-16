# Given a directed graph of N nodes where each node is pointing to exactly one of the N nodes (can possibly
# point to itself). Ishu, the coder, is bored and he has discovered a problem out of it to keep himself busy.
# Problem is as follows:
# A node is 'good' if it satisfies one of the following:
# 1. It is the special node (marked as node 1)
# 2. It is pointing to the special node (node 1)
# 3. It is pointing to a good node.
# Ishu is going to change pointers of some nodes to make them all 'good'. You have to find the minimum number of
# pointers to change in order to make all the nodes good (Thus, a Good Graph).
# NOTE: Resultant Graph should hold the property that all nodes are good and each node must point to exactly one node.
# 1 <= N <= 10^5
# First and only argument is an integer array A containing N numbers all between 1 to N, where i-th number
# is the number of node that i-th node is pointing to.
# An Integer denoting minimum number of pointer changes.
class Solution:
    def find(self, parent, node):
        if node == parent[node]:
            return node
        return self.find(parent, parent[node])

    def unionNodes(self, a, b, parent, size):
        a = self.find(parent, a)
        b = self.find(parent, b)

        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            size[a] += size[b]
            parent[b] = a

    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        pairList = []
        parent = [0 for _ in range(N + 1)]
        size = [0 for _ in range(N + 1)]

        for i in range(N):
            pairList.append((i + 1, A[i]))

        for i in range(N + 1):
            parent[i] = i
            size[i] = 1

        for i in range(N):
            if pairList[i][0] == 1:
                self.unionNodes(pairList[i][0], pairList[i][1], parent, size)
            elif pairList[i][1] == 1:
                self.unionNodes(pairList[i][1], pairList[i][0], parent, size)
            else:
                self.unionNodes(pairList[i][0], pairList[i][1], parent, size)

        temp = set()
        for node in parent:
            temp.add(node)

        result = len(temp)
        if 1 in temp:
            result -= 1
        if 0 in temp:
            result -= 1

        return result


sol = Solution()
print(sol.solve([1, 2, 1, 2]))  # 1
print(sol.solve([3, 1, 3, 1]))  # 1
