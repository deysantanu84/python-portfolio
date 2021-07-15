# Given an array A of N integers, find the index of values that satisfy P + Q = R + S,
# where P,Q,R & S are integers values in the array
# Expected time complexity O(N2)
# NOTE:
# 1) Return the indices `A1 B1 C1 D1`, so that
#   A[A1] + A[B1] = A[C1] + A[D1]
#   A1 < B1, C1 < D1
#   A1 < C1, B1 != D1, B1 != C1
# 2) If there are more than one solutions,
#    then return the tuple of values which are lexicographical smallest.
# Assume we have two solutions
# S1 : A1 B1 C1 D1 ( these are values of indices in the array )
# S2 : A2 B2 C2 D2
# S1 is lexicographically smaller than S2 if:
#   A1 < A2 OR
#   A1 = A2 AND B1 < B2 OR
#   A1 = A2 AND B1 = B2 AND C1 < C2 OR
#   A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
# If no solution is possible, return an empty list.
# indexes returned should be 0-based.
def equals(A):
    result = []
    indexDict = {}

    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            tempSum = A[i] + A[j]
            if tempSum in indexDict.keys():
                if indexDict[tempSum][0] < i \
                        and indexDict[tempSum][1] != i \
                        and indexDict[tempSum][1] != j:
                    currResult = [indexDict[tempSum][0], indexDict[tempSum][1], i, j]
                    if len(result) == 0 or result > currResult:
                        result = currResult
            else:
                indexDict[tempSum] = (i, j)
    return result


print(equals([3, 4, 7, 1, 2, 9, 8]))  # [0, 2, 3, 5]
print(equals([2, 5, 1, 6]))  # [0, 1, 2, 3]
