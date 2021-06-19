# Given eight integers A, B, C, D, E, F, G and H which represent two rectangles in a 2D plane.
# For the first rectangle it's bottom left corner is (A, B) and top right corner is (C, D)
# and for the second rectangle it's bottom left corner is (E, F) and top right corner is (G, H).
# Find and return whether the two rectangles overlap or not.
# -10000 <= A < C <= 10000
# -10000 <= B < D <= 10000
# -10000 <= E < G <= 10000
# -10000 <= F < H <= 10000
# Return 1 if the two rectangles overlap else return 0.
# A = 0   B = 0
# C = 4   D = 4
# E = 2   F = 2
# G = 6   H = 6
# 1 --- rectangle with bottom left (2,2) and top right (4,4) is overlapping.
# A = 0   B = 0
# C = 4   D = 4
# E = 2   F = 2
# G = 3   H = 3
# 1 --- overlapping rectangles can be found
# l1 = (A, B)
# r1 = (C, D)
def rectanglesOverlap(A, B, C, D, E, F, G, H):
    if A >= G or E >= C:
        return 0
    if D <= F or H <= B:
        return 0
    return 1


print(rectanglesOverlap(0, 0, 4, 4, 2, 2, 6, 6))  # 1
print(rectanglesOverlap(0, 0, 4, 4, 2, 2, 3, 3))  # 1
