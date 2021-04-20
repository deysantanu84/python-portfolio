# Given an array of integers A, we call (i, j) an important reverse pair if i < j and A[i] > 2*A[j].
# Return the number of important reverse pairs in the given array A.
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 10^9
# https://leetcode.com/problems/reverse-pairs/discuss/821776/Python%3A-Simple-Solution-based-on-Merge-Sort-oror-Time-O(n*logn)
count = 0


def merge(left, right):
    global count
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= 2 * right[j]:
            i += 1
        else:
            count += len(left) - i
            j += 1

    return sorted(left + right)


def mergeSort(A):
    if len(A) <= 1:
        return A
    return merge(mergeSort(A[:(len(A) + 1) // 2]), mergeSort(A[(len(A) + 1) // 2:]))


def reversePairs(A):
    global count
    count = 0
    mergeSort(A)
    return count


print(reversePairs([1, 3, 2, 3, 1]))  # 2
print(reversePairs([4, 1, 2]))  # 1
