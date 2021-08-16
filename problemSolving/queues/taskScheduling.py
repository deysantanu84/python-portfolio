# A CPU has N tasks to be performed. It is to be noted that the tasks have to be performed in a specific order
# to avoid deadlock. In every clock cycle the CPU can either perform a task or move it to the back of the queue.
# You are given the current state of the scheduler queue in an array A and the required order of the tasks in
# an array B.
# Determine the minimum number of clock cycles to complete all the tasks.
# 1 <= N <= 1000
# 1 <= A[i], B[i] <= N
# First argument consist of integer array A.
# Second argument consist of integer array B.
# Return an integer denoting the minimum number of clock cycles required to complete all the tasks.
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        result = 0
        queue = []

        for i in range(len(A)):
            queue.append(A[i])

        for i in range(len(B)):
            while len(queue) and queue[0] != B[i]:
                queue.append(queue.pop(0))
                result += 1

            if queue[0] == B[i]:
                queue.pop(0)
                result += 1

        return result


sol = Solution()
print(sol.solve([2, 3, 1, 5, 4], [1, 3, 5, 4, 2]))  # 10
print(sol.solve([1], [1]))  # 1
