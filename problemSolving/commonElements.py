# Given two integer array A and B of size N and M respectively.
# Your task is to find all the common elements in both the array.
# NOTE: Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# A = [1, 2, 2, 1], B = [2, 3, 1, 2] ---> [1, 2, 2]
# A = [2, 1, 4, 10], B = [3, 6, 2, 10, 10] ---> [2, 10]
# https://stackoverflow.com/questions/37645053/intersection-of-two-lists-including-duplicates
from collections import Counter


def commonElements(A, B):
    return list((Counter(A) & Counter(B)).elements())


print(commonElements([1, 2, 2, 1], [2, 3, 1, 2]))
print(commonElements([2, 1, 4, 10], [3, 6, 2, 10, 10]))
