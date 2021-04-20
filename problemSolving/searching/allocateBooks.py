# Given an array of integers A of size N and an integer B.
# College library has N books, the ith book has A[i] number of pages.
# You have to allocate books to B number of students so that
# maximum number of pages allotted to a student is minimum.
# A book will be allocated to exactly one student.
# Each student has to be allocated at least one book.
# Allotment should be in contiguous order, for example:
# A student cannot be allocated book 1 and book 3, skipping book 2.
# Calculate and return that minimum possible number.
# NOTE: Return -1 if a valid assignment is not possible.
import sys
INT_MAX = sys.maxsize - 1


def isValid(A, B, x):
	N = len(A)
	count = 1
	tempSum = 0

	for i in range(N):
		if A[i] > x:
			return False

		if tempSum + A[i] > x:
			count += 1
			tempSum = A[i]
			if count > B:
				return False
		else:
			tempSum += A[i]

	return True


def allocateBooks(A, B):
	N = len(A)
	pageCount = 0
	if N < B:
		return -1

	for i in range(N):
		pageCount += A[i]

	start = 0
	end = pageCount
	result = INT_MAX

	while start <= end:
		mid = start + (end - start) // 2
		if isValid(A, B, mid):
			result = min(result, mid)
			end = mid - 1
		else:
			start = mid + 1

	return result


print(allocateBooks([12, 34, 67, 90], 2))  # 113
