# There is a corridor in a jail which is N units long. Given an array A of size N.
# The ith index of this array is 0 if the light at ith position is faulty otherwise it is 1.
# All the lights are of specific power B which if is placed at position X, it can light the
# corridor from [X-B+1, X+B-1]. Initially lights are off.
# Return the minimum number of lights to be turned ON to light the whole corridor
# or -1 if the whole corridor cannot be lighted
def findMinLights(A, B):
    lightsLit = {}
    minLightsList = []

    for index1 in range(len(A)):
        currLightsList = []
        for index in range(len(A)):
            lightsLit[index] = False
        for index in range(index1, len(A)):
            # print(index, currLightsList, lightsLit)
            if A[index] == 1 and not lightsLit[index]:
                currLightsList.append(index)
                for i in range((index - B + 1), (index + B)):
                    if i in lightsLit.keys():
                        lightsLit[i] = True

        if minLightsList and currLightsList:
            if len(minLightsList) > len(currLightsList):
                minLightsList = currLightsList

        elif not minLightsList and currLightsList:
            minLightsList = currLightsList

    if not len(minLightsList):
        return -1
    else:
        print(minLightsList)
        return len(minLightsList)


P = [0, 0, 1, 1, 1, 0, 0, 1]
Q = 3
print(findMinLights(P, Q))
P = [0, 0, 0, 1, 0]
Q = 3
print(findMinLights(P, Q))
P = [1, 1, 1, 1]
Q = 3
print(findMinLights(P, Q))
P = [1, 1, 1]
Q = 6
print(findMinLights(P, Q))
