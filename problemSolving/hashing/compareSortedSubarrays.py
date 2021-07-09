# Given an array A of length N. You have to answer Q queries.
# Each query will contain 4 integers l1, r1, l2 and r2.
# If sorted segment from [l1, r1] is same as sorted segment from [l2 r2] then answer is 1 else 0.
# NOTE The queries are 0-indexed.
# 0 <= A[i] <= 100000
# 1 <= N <= 100000
# 1 <= Q <= 100000
# First argument is an array A.
# Second will be 2-D array B denoting queries with dimension Q * 4.
# Consider ith query as l1 = B[i][0], r1 = B[i][1], l2 = A[i][2], r2 = B[i][3].
# Return an array of length Q with answer of the queries in the same order in input.
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        result = []
        # Brute force - TLE
        # for query in B:
        #     if sorted(A[query[0]: query[1] + 1]) == sorted(A[query[2]: query[3] + 1]):
        #         result.append(1)
        #     else:
        #         result.append(0)

        queryDict = {}
        for query in B:
            isSorted = True
            stack = []

            temp = (query[0], query[1], query[2], query[3])

            if temp in queryDict.keys():
                result.append(queryDict[temp])
                continue

            if query[1] - query[0] != query[3] - query[2]:
                queryDict[temp] = 0
                result.append(0)
                continue

            for index in range(query[0], query[1] + 1):
                stack.append(A[index])

            for index in range(query[2], query[3] + 1):
                if A[index] not in stack:
                    queryDict[temp] = 0
                    isSorted = False
                    result.append(0)
                    break

            if isSorted:
                queryDict[temp] = 1
                result.append(1)

        return result


sol = Solution()
print(sol.solve([1, 7, 11, 8, 11, 7, 1], [[0, 2, 4, 6]]))  # [1]
print(sol.solve([1, 3, 2], [[0, 1, 1, 2]]))  # [0]
