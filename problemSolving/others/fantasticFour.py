def solve(A):
    count = 0
    tempDict = {}
    for item in A:
        if item % 4:
            tempDict[item] = 0

    for item in A:
        if item % 4:
            tempDict[item] += 1

    for item in tempDict.keys():
        print(item, tempDict)
        if tempDict[item] != 0:
            if (4 - item) in tempDict.keys() and tempDict[4 - item] != 0:
                if item == 4 - item and tempDict[4 - item] == 1:
                    continue
                A.remove(4 - item)
                A.remove(item)
                A.append(4)
                tempDict[4 - item] -= 1
                tempDict[item] -= 1
                count += 1

    print(tempDict)
    for value in tempDict.values():
        if value > 0:
            return -1
    else:
        return count


# print(solve([1, 3, 4, 4, 2, 2]))  # 2
# print(solve([4, 2, 2]))  # 1
# print(solve([1, 2, 3, 1, 2, 3, 8]))  # 3
# print(solve([4, 4, 4, 4]))  # 0
# print(solve([1, 1, 3, 2]))  # -1
print(solve([2, 2, 2, 2]))  # 2
