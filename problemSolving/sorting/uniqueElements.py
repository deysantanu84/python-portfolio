# You are given an array A of N elements.
# You have to make all elements unique, to do so in one step you can increase any number by one.
# Find the minimum number of steps.
# 1 <= N <= 10^5
# 1 <= A[i] <= 10^9
def uniqueElements(A):
    count = 0
    A.sort(reverse=True)
    uniqueSet = set()
    emptySlot = [A[0] + 1]
    uniqueSet.add(A[0])
    for item in A[1:]:
        if item in uniqueSet:
            temp = emptySlot.pop(-1)
            count += temp - item
            if temp + 1 not in uniqueSet:
                emptySlot.append(temp + 1)
            uniqueSet.add(temp)
        else:
            if item + 1 not in uniqueSet:
                emptySlot.append(item + 1)
            uniqueSet.add(item)
    return count


print(uniqueElements([1, 1, 3]))  # 1
print(uniqueElements([2, 4, 5]))  # 0
print(uniqueElements([51, 6, 10, 8, 22, 61, 56, 48, 88, 85, 21, 98, 81, 76, 71, 68, 18, 6, 14, 23, 72, 18, 56, 30, 97, 100, 81, 5, 99, 2, 85, 67, 46, 32, 66, 51, 76, 53, 36, 31, 81, 56, 26, 75, 69, 54, 54, 54, 83, 41, 86, 48, 7, 32, 85, 23, 47, 23, 18, 45, 79, 95, 73, 15, 55, 16, 66, 73, 13, 85, 14, 80, 39, 92, 66, 20, 22, 25, 34, 14, 51, 14, 17, 10, 100, 35, 9, 83, 31, 60, 24, 37, 69, 62]))  # 239
