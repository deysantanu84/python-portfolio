def solve(A):
    twoDimList = []
    for i in range(1, A+1):
        oneDimList = []
        for j in range(1, i+1):
            oneDimList.append(j)
        twoDimList.append(oneDimList)

    return twoDimList


print(solve(4))
