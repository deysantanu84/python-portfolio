# Max Heap is a special kind of complete binary tree in which for every node
# the value present in that node is greater than the value present in it’s children nodes.
# Find the number of distinct Max Heap can be made from A distinct integers.
# In short, you have to ensure the following properties for the max heap :
# Heap has to be a complete binary tree ( A complete binary tree is a binary tree in which every level,
# except possibly the last, is completely filled, and all nodes are as far left as possible.)
# Every node is greater than all its children.
# NOTE: If you want to know more about Heaps, please visit this link. Return your answer modulo 10^9 + 7.
# 1 <= A <= 100
# First and only argument is an integer A.
# Return an integer denoting the number of distinct Max Heap.
class Solution:
    def combinations(self, N, R):
        if 2 * R > N:
            return self.combinations(N, N - R)

        count = 1

        for i in range(R):
            count = count * (N - i) // (i + 1)

        return count

    # @param A : integer
    # @return an integer
    def solve(self, A):
        result = [1, 1]
        level = 0

        for index in range(2, A + 1):
            if 2 << level <= index:
                level += 1

            mid = index - (1 << level) + 1
            left = (1 << (level - 1)) - 1 + min(mid, 1 << (level - 1))
            right = (1 << (level - 1)) - 1 + max(0, mid - (1 << (level - 1)))
            heaps = (self.combinations(index - 1, left) * result[left] * result[right]) % (10**9 + 7)
            result.append(heaps)

        return result[A]


heap = Solution()
print(heap.solve(4))  # 3
print(heap.solve(10))  # 3360
