# Tom and Harry are given N numbers, with which they play a game as a team.
# Initially, Tom chooses a particular number P from the N numbers,
# and he takes away all the numbers that are equal to P.
# Next, Harry chooses a different number Q, different from what Tom chose,
# and takes away all the numbers equal to Q from the remaining N numbers.
# They win the game if they can take all the numbers by doing the above operation once
# and if each of them has the same amount of numbers towards the end.
# If they win, return the string "WIN", else return "LOSE".
def perfectCards(A):
    tomCount = 0
    harryCount = 0
    if len(A):
        P = A[0]
        while P in A:
            A.remove(P)
            tomCount += 1

    if len(A):
        Q = A[0]
        while Q in A:
            A.remove(Q)
            harryCount += 1

    if len(A) == 0 and tomCount == harryCount:
        return "WIN"

    return "LOSE"


print(perfectCards([1, 2]))  # "WIN"
print(perfectCards([6, 6]))  # "LOSE"
print(perfectCards([1, 1, 2, 2, 3]))  # "LOSE"
