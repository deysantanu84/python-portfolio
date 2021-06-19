# Given a stack of integers A, sort it using another stack.
# Return the array of integers after sorting the stack using another stack.
# 1 <= |A| <= 5000
# 0 <= A[i] <= 1000000000
def sortStackWithAnotherStack(A):
    result = []

    while len(A):
        temp = A[-1]
        A.pop()

        while len(result) and int(result[-1]) > int(temp):
            A.append(result[-1])
            result.pop()

        result.append(temp)

    return result


print(sortStackWithAnotherStack([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
print(sortStackWithAnotherStack([5, 17, 100, 11]))  # [5, 11, 17, 100]
