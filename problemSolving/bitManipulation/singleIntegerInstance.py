# Given an array of integers A, every element appears twice except for one. Find that single one.
# NOTE: Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?
def solve(A):
    result = 0
    for item in A:
        # print('Result: ', result, '\titem: ', item)
        result ^= item

    return result


inputArray = [1, 2, 2, 3, 1]
# inputArray = [1, 2, 2]
print(solve(inputArray))
