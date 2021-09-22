def maximumProduct(inputArray):
    mod = 10 ** 9 + 7
    N = len(inputArray)
    inputArray.sort()

    powerList = [0] * (N + 1)
    powerList[0] = 1

    for index in range(1, N + 1):
        powerList[index] = 2 * powerList[index - 1]
        powerList[index] %= mod

    result = 1

    for index in range(N - 1, -1, -1):
        value = (powerList[index] - 1)

        for index1 in range(value):
            result *= inputArray[index]
            result %= mod

    for index in range(N):
        result *= inputArray[index]
        result %= mod

    return result


print(maximumProduct([3, 7]))  # 147
print(maximumProduct([4, 7]))  # 196
