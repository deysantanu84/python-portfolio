# Given two arrays of integers A and B of size N each, where each pair (A[i], B[i])
# for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.
# Find and return the number of unordered triplets (i, j, k) such that
# (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right angled triangle
# with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.
# NOTE: The answer may be large so return the answer modulo (10^9 + 7).
# 1 <= N <= 10^5
# 0 <= A[i], B[i] <= 10^9
def countRightTriangles(A, B):
    result = 0
    points = []
    for i in range(len(A)):
        point = (A[i], B[i])
        points.append(point)

    xFreqDict = {}
    yFreqDict = {}

    for item in A:
        if item in xFreqDict.keys():
            xFreqDict[item] += 1
        else:
            xFreqDict[item] = 1

    for item in B:
        if item in yFreqDict.keys():
            yFreqDict[item] += 1
        else:
            yFreqDict[item] = 1

    for point in points:
        result += (xFreqDict[point[0]] - 1) * (yFreqDict[point[1]] - 1)

    return result


print(countRightTriangles([1, 1, 2], [1, 2, 1]))  # 1
print(countRightTriangles([1, 1, 2, 3, 3], [1, 2, 1, 2, 1]))  # 6
