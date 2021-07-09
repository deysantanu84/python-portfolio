# You are given an array A containing N numbers. This array is called special
# if it satisfies one of the following properties:
# There exists an element A[i] in the array such that A[i] is equal to the
# median of elements [A[0], A[1], ...., A[i-1]]
# There exists an element A[i] in the array such that A[i] is equal to the
# median of elements [A[i+1], A[i+2], ...., A[N-1]]
# Median is the middle element in the sorted list of elements. If the number of elements are even then median will be (sum of both middle elements)/2.
# Return 1 if the array is special else return 0.
# NOTE:
# For A[0] consider only the median of elements [A[1], A[2], ..., A[N-1]] (as there are no elements to the left of it)
# For A[N-1] consider only the median of elements [A[0], A[1], ...., A[N-2]]
