# You have an array A with N elements. We have 2 types of operation available on this array :
# We can split a element B into 2 elements C and D such that B = C + D.
# We can merge 2 elements P and Q as one element R such that R = P^Q i.e XOR of P and Q.
# You have to determine whether it is possible to make array A containing only 1 element
# i.e. 0 after several splits and/or merge?
# 1 <= N <= 100000
# 1 <= A[i] <= 10^6
# Return "Yes" if it is possible otherwise return "No".
def interestingArray(A):
    pass


print(interestingArray([9, 17]))  # Yes
# Following is one possible sequence of operations -
# 1) Merge i.e 9 XOR 17 = 24
# 2) Split 24 into two parts each of size 12
# 3) Merge i.e 12 XOR 12 = 0
# As there is only 1 element i.e 0. So it is possible.

print(interestingArray([1]))  # No
# There is no possible way to make it 0.
