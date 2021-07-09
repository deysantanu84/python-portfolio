# Given an array of integers A denoting a stream of integers. New arrays of integer B and C are
# formed. Each time an integer is encountered in a stream, append it at the end of B and append
# median of array B at the C. Find and return the array C.
# NOTE:
# If the number of elements are N in B and N is odd then consider median as B[N/2]
# ( B must be in sorted order).
# If the number of elements are N in B and N is even then consider median as B[N/2-1].
# ( B must be in sorted order).
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 10^9
# The only argument given is the integer array A.
# Return an integer array C, C[i] denotes the median of first i elements.
from heapq import heappush, heappop


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)
        maxHeap = []
        minHeap = []
        result = []

        median = A[0]
        heappush(maxHeap, -1 * median)
        result.append(median)

        for index in range(1, N):
            temp = A[index]
            if len(maxHeap) > len(minHeap):
                if temp < median:
                    heappush(minHeap, -1 * maxHeap[0])
                    heappop(maxHeap)
                    heappush(maxHeap, -1 * temp)
                else:
                    heappush(minHeap, temp)

                median = -1 * maxHeap[0]

            elif len(maxHeap) == len(minHeap):
                if temp < median:
                    heappush(maxHeap, -1 * temp)
                    median = -1 * maxHeap[0]
                else:
                    heappush(minHeap, temp)
                    median = minHeap[0]

            else:
                if temp > median:
                    heappush(maxHeap, -1 * minHeap[0])
                    heappop(minHeap)
                    heappush(minHeap, temp)
                else:
                    heappush(maxHeap, -1 * temp)

                median = -1 * maxHeap[0]

            result.append(median)

        return result


sol = Solution()
print(sol.solve([1, 2, 5, 4, 3]))  # [1, 1, 2, 2, 3]
print(sol.solve([5, 17, 100, 11]))  # [5, 5, 17, 11]
print(sol.solve([69, 52, 34, 19, 56, 57, 5, 3, 83, 56]))  # [69, 52, 52, 34, 52, 52, 52, 34, 52, 52]
