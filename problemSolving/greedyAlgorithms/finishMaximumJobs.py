# There are N jobs to be done but you can do only one job at a time.
# Given an array A denoting the start time of the jobs and
# an array B denoting the finish time of the jobs.
# Your aim is to select jobs in such a way so that you can finish maximum number of jobs.
# Return the maximum number of jobs you can finish.
# 1 <= N <= 10^5
# 1 <= A[i] < B[i] <= 10^9
# First argument is an integer array A of size N denoting the start time of the jobs.
# Second argument is an integer array B of size N denoting the finish time of the jobs.
# Return an integer denoting the maximum number of jobs you can finish.
class Job:
    def __init__(self, start=0, finish=0):
        self.start = start
        self.finish = finish


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        jobs = [Job() for _ in range(len(A))]

        for i in range(len(A)):
            jobs[i] = Job(A[i], B[i])

        jobs.sort(key=lambda x: x.finish)
        result = 1

        previous = jobs[0]
        for i in range(1, len(A)):
            temp = jobs[i]
            if temp.start >= previous.finish:
                result += 1
                previous = temp

        return result


sol = Solution()
print(sol.solve([1, 5, 7, 1], [7, 8, 8, 8]))  # 2
print(sol.solve([3, 2, 6], [9, 8, 9]))  # 1
