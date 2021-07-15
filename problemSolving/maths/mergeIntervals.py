# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.
# Input:: First argument is the vector of intervals. Second argument is the new interval to be merged
# Output: Return the vector of intervals after merging
# Given intervals [1, 3], [6, 9] insert and merge [2, 5] . [ [1, 5], [6, 9] ]
# Given intervals [1, 3], [6, 9] insert and merge [2, 6] . [ [1, 9] ]
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution2:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    @staticmethod
    def insert(A, B):
        N = len(A)
        for interval in A:
            if interval.start > interval.end:
                interval.start, interval.end = interval.end, interval.start
            print(interval.start, interval.end)

        if B.start > B.end:
            B.start, B.end = B.end, B.start
        print(B.start, B.end)

        mergedList = [A[0]]
        topInterval = mergedList[len(mergedList) - 1]
        if B.start < topInterval.end:
            mergedList.pop()
            topInterval.start = min(topInterval.start, B.start)
            topInterval.end = max(topInterval.end, B.end)
            mergedList.append(topInterval)
        else:
            mergedList.append(B)

        for i in range(1, N):
            topInterval = mergedList[len(mergedList) - 1]
            if A[i].start <= topInterval.end:
                mergedList.pop()
                topInterval.start = min(topInterval.start, A[i].start)
                topInterval.end = max(topInterval.end, A[i].end)
                mergedList.append(topInterval)
            else:
                mergedList.append(A[i])

        return mergedList


class Solution:
    @staticmethod
    def insert(A, B):
        if len(A) == 0:
            return [B]

        if A[-1].end < B.start:
            return A + [B]

        if B.end < A[0].start:
            return [B] + A

        mergedList = []
        i = 0
        for interval in A:
            if interval.end < B.start:
                mergedList.append(interval)
            else:
                tempInterval = Interval()
                tempInterval.start = min(interval.start, B.start)
                tempInterval.end = B.end
                i = A.index(interval)

                while i < len(A) and tempInterval.end >= A[i].start:
                    tempInterval.end = max(A[i].end, B.end)
                    i += 1
                mergedList.append(tempInterval)
                break

        mergedList += A[i:]
        return mergedList


result = Solution()
# a = Interval(1, 2)
# b = Interval(3, 6)
# c = Interval(8, 10)
a = Interval(1, 3)
b = Interval(6, 9)
c = Interval(2, 6)

for item in result.insert([a, b], c):
    print(item.start, item.end)
# print(mergeIntervals([[1, 3], [6, 9]], [2, 5]))  # [ [1, 5], [6, 9] ]
# print(mergeIntervals([[1, 3], [6, 9]], [2, 6]))  # [ [1, 9] ]
# print(mergeIntervals([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9]))  # [[1, 2], [3, 10], [12, 16]]
# [ (1, 2), (3, 6) ], (10, 8)  # [(1, 2), (3, 6), (8, 10)]
