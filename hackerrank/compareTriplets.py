# https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Complete the compareTriplets function below.
def compareTriplets(aliceRatingList, bobRatingList):
    aliceScore = 0
    bobScore = 0
    for i in range(len(aliceRatingList)):
        if aliceRatingList[i] > bobRatingList[i]:
            aliceScore += 1
        elif aliceRatingList[i] < bobRatingList[i]:
            bobScore += 1

    return [aliceScore, bobScore]


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(result)
