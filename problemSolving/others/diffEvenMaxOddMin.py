# You are given an array of integers A of size N.
# Return the difference between the maximum among all even numbers of A
# and the minimum among all odd numbers in A.
def solve(A):
    # Create list of even elements evenList
    evenList = []
    # Create list of odd elements oddList
    oddList = []

    # Populate both lists from elements in A
    for item in A:
        if item % 2:
            oddList.append(item)
        else:
            evenList.append(item)

    return sorted(evenList)[-1] - sorted(oddList)[0]


# inputArray = [0, 2, 9]
inputArray = [5, 17, 100, 1]
print(solve(inputArray))
