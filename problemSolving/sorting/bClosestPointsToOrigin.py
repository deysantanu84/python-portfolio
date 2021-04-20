# We have a list A, of points(x,y) on the plane. Find the B closest points to the origin (0, 0).
# Here, the distance between two points on a plane is the Euclidean distance.
# You may return the answer in any order.
# The answer is guaranteed to be unique (except for the order that it is in.)
# NOTE: Euclidean distance between two points P1(x1,y1) and P2(x2,y2) is sqrt((x1-x2)^2 + (y1-y2)^2).
# 1 <= B <= length of the list A <= 100000
# -100000 <= A[i][0] <= 100000
# -100000 <= A[i][1] <= 100000
def bClosestPointsToOrigin(A, B):
	A.sort(key=lambda P: P[0]**2 + P[1]**2)
	return A[:B]


print(bClosestPointsToOrigin([[3, 3], [5, -1], [-2, 4]], 2))  # [[3, 3], [-2, 4]]
print(bClosestPointsToOrigin([[1, 3], [-2, 2]], 1))  # [[-2, 2]]
print(bClosestPointsToOrigin([[1, -1], [2, -1]], 1))  # [[1, -1]]
