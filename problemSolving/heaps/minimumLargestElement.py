# Given an array A of N numbers, you have to perform B operations.
# In each operation, you have to pick any one of the N elements and add original value
# (value stored at index before we did any operations) to it's current value.
# You can choose any of the N elements in each operation.
# Perform B operations in such a way that the largest element of the modified array (after B operations)
# is minimised. Find the minimum possible largest element after B operations.
# 1 <= N <= 10^6
# 0 <= B <= 10^5
# -105 <= A[i] <= 10^5
# First argument is an integer array A.
# Second argument is an integer B.
# Return an integer denoting the minimum possible largest element after B operations.
from heapq import heappush, heappop


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        heap = []
        curr = A.copy()

        for i in range(N):
            heappush(heap, (2 * A[i], i))

        while B:
            index = heap[0][1]
            curr[index] += A[index]
            heappop(heap)
            heappush(heap, (curr[index] + A[index], index))

            B -= 1

        return max(curr)


sol = Solution()
print(sol.solve([1, 2, 3, 4], 3))  # 4
# Apply operation on element at index 0, the array would change to [2, 2, 3, 4]
# Apply operation on element at index 0, the array would change to [3, 2, 3, 4]
# Apply operation on element at index 0, the array would change to [4, 2, 3, 4]
# Minimum possible largest element after 3 operations is 4.

print(sol.solve([5, 1, 4, 2], 5))  # 5
# Apply operation on element at index 1, the array would change to [5, 2, 4, 2]
# Apply operation on element at index 1, the array would change to [5, 3, 4, 2]
# Apply operation on element at index 1, the array would change to [5, 4, 4, 2]
# Apply operation on element at index 1, the array would change to [5, 5, 4, 2]
# Apply operation on element at index 3, the array would change to [5, 5, 4, 4]
# Minimum possible largest element after 5 operations is 5.

print(sol.solve([8, 6, 4, 2], 8))  # 12
