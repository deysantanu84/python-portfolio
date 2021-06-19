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
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        jobs = []
        for i in range(len(A)):
            job = [A[i], B[i]]
            jobs.append(job)

        jobs = sorted(jobs, key=lambda x: x[1])
        visited = set()

        for start, end in jobs:
            for task in range(start, end + 1):
                if task not in visited:
                    visited.add(task)
                    break

        return len(visited)


sol = Solution()
print(sol.solve([1, 5, 7, 1], [7, 8, 8, 8]))  # 2
print(sol.solve([3, 2, 6], [9, 8, 9]))  # 1
