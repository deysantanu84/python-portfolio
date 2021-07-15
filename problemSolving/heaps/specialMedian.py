# You are given an array A containing N numbers. This array is called special
# if it satisfies one of the following properties:
# There exists an element A[i] in the array such that A[i] is equal to the
# median of elements [A[0], A[1], ...., A[i-1]]
# There exists an element A[i] in the array such that A[i] is equal to the
# median of elements [A[i+1], A[i+2], ...., A[N-1]]
# Median is the middle element in the sorted list of elements. If the number of elements are even then median
# will be (sum of both middle elements)/2.
# Return 1 if the array is special else return 0.
# NOTE:
# For A[0] consider only the median of elements [A[1], A[2], ..., A[N-1]] (as there are no elements to the left of it)
# For A[N-1] consider only the median of elements [A[0], A[1], ...., A[N-2]]
class Solution:
    def findMedian(self, arr):
        n = len(arr)
        arr.sort()
        if n < 1:
            return None
        if n % 2 == 0:
            return (arr[(n // 2) - 1] + arr[n // 2]) // 2
        else:
            return arr[(n - 1) // 2]

    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        if A[0] == self.findMedian(A[1:]) or A[-1] == self.findMedian(A[: -1]):
            return 1

        for i in range(1, N - 1):
            if A[i] == self.findMedian(A[: i]) or A[i] == self.findMedian(A[i + 1:]):
                return 1

        return 0


sol = Solution()
print(sol.solve([4, 6, 8, 4]))  # 1
print(sol.solve([2, 7, 3, 1]))  # 0
print(sol.solve([2, 4, 3]))  # 1
