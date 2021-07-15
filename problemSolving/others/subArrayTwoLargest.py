# You are given an array of distinct integers A, you have to find and return all elements
# in array which have at-least two greater elements than themselves.
# NOTE: The result should have the order in which they are present in the original array.
def solve(A):
    for i in range(2):
        largest = sorted(A)[-1]
        while largest in A:
            A.remove(largest)

    return A


inputArray = [1, 2, 3, 4, 5]
# inputArray = [391, 634, 740, 441, 75, 444, 65, 611, 679, 59, 878, 102, 42, 190, 801, 571, 79, 686, 523, 580, 199, 497, 879, 334, 200, 202, 991, 341, 479, 563, 112, 550, 494, 468, 56, 644, 53, 581, 836, 461, 905, 849, 838, 434, 818, 350, 585, 280, 252, 834, 510, 420, 395, 776, 118, 886, 19, 809, 534, 143, 933, 15, 999, 514, 230, 531, 666, 841, 861, 703, 972, 622, 640, 21, 811, 476, 751, 430, 308, 996, 165, 812, 424, 412, 903, 601, 226, 239, 728, 135]
print(solve(inputArray))
