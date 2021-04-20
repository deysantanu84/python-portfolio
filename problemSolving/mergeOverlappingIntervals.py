# Given a collection of intervals, merge all overlapping intervals.
# 1 <= Total number of intervals <= 100000.
# Return the sorted list of intervals after merging all the overlapping intervals.
# [1,3],[2,6],[8,10],[15,18]  # [1,6],[8,10],[15,18]


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    @staticmethod
    def merge(intervals):
        if len(intervals) == 0:
            return intervals

        intervals.sort(key=lambda x: x.start)
        mergedList = []
        mergedInterval = intervals[0]

        for i in range(1, len(intervals)):
            if mergedInterval.end >= intervals[i].start:
                if intervals[i].end >= mergedInterval.end:
                    closingInterval = intervals[i].end
                else:
                    closingInterval = mergedInterval.end
                mergedInterval.end = closingInterval
            else:
                mergedList.append(mergedInterval)
                mergedInterval = intervals[i]

        if len(mergedList) == 0 or mergedList[-1] != mergedInterval:
            mergedList.append(mergedInterval)

        return mergedList


result = Solution()
a = Interval(1, 3)
b = Interval(2, 6)
c = Interval(8, 10)
d = Interval(15, 18)
for item in result.merge([a, b, c, d]):
    print(item.start, item.end)
