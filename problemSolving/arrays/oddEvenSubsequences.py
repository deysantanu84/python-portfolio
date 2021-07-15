# Given an array of integers A of size N. Find the longest subsequence of A which is odd-even.
# A subsequence is said to odd-even in the following cases:
# The first element of the subsequence is odd, second element is even, third element is odd and so on.
# For example: [5, 10, 5, 2, 1, 4], [1, 2, 3, 4, 5]
# The first element of the subsequence is even, second element is odd, third element is even and so on.
# For example: [10, 5, 2, 1, 4, 7], [10, 1, 2, 3, 4]
# Return the maximum possible length of odd-even subsequence.
# Note: An array B is a subsequence of an array A if B can be obtained from A by
# deletion of several (possibly, zero or all) elements.
# https://medium.com/@kaustubhdwivedi1729/longest-odd-even-subsequence-7b32578b9f08
odd = False
even = False


def solve(A):
    global odd, even
    count = 1
    result = [A[0]]
    # first entry is odd
    if A[0] % 2:
        odd = False
        even = True
        for i in range(1, len(A)):
            if odd and A[i] % 2:
                result.append(A[i])
                count += 1
                odd = False
                even = True
            elif even and not A[i] % 2:
                result.append(A[i])
                count += 1
                odd = True
                even = False

    # first entry is even
    else:
        odd = True
        even = False
        for i in range(1, len(A)):
            if odd and A[i] % 2:
                result.append(A[i])
                count += 1
                odd = False
                even = True
            elif even and not A[i] % 2:
                result.append(A[i])
                count += 1
                odd = True
                even = False

    print(result)
    return count


# print(solve([1, 2, 2, 5, 6]))
# print(solve([2, 2, 2, 2, 2, 2]))
print(solve([16, 19, 13, 43, 21, 47, 20]))
