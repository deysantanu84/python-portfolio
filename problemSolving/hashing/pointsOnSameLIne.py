# Given two array of integers A and B describing a pair of (A[i], B[i]) coordinates in 2D plane.
# A[i] describe x coordinates of the ith point in 2D plane whereas B[i] describes
# the y-coordinate of the ith point in 2D plane.
# Find and return the maximum number of points which lie on the same line.
def pointsOnSameLine(A, B):
    points = []
    for i in range(len(A)):
        point = (A[i], B[i])
        points.append(point)

    N = len(points)

    if N < 3:
        return N

    result = 0

    for i in points:
        pointDict = {}
        duplicateCount = 0
        currMax = 0

        for j in points:
            if i != j:
                if j[0] == i[0]:
                    slope = 'inf'
                else:
                    slope = float(j[1] - i[1]) / float(j[0] - i[0])

                pointDict[slope] = pointDict.get(slope, 0)+1
                currMax = max(currMax, pointDict[slope])

            else:
                duplicateCount += 1

        result = max(result, currMax + duplicateCount)

    return result


print(pointsOnSameLine([-1, 0, 1, 2, 3, 3], [1, 0, 1, 2, 3, 4]))  # 4
print(pointsOnSameLine([3, 1, 4, 5, 7, -9, -8, 6], [4, -8, -3, -2, -1, 5, 7, -4]))  # 2
