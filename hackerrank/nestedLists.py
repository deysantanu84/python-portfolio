# https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    scoresList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scoresList.append([name, score])

    # sort nested list by second entry of sub-list
    scoresList = sorted(scoresList, key=lambda x: x[1])
    lowestScore = scoresList[0][1]
    secondLowestScoreList = []
    i = 0
    while i < len(scoresList) and scoresList[i][1] == lowestScore:
        i += 1

    secondLowestScore = scoresList[i][1]
    while i < len(scoresList) and scoresList[i][1] == secondLowestScore:
        secondLowestScoreList.append(scoresList[i][0])
        i += 1

    for name in sorted(secondLowestScoreList):
        print(name)
