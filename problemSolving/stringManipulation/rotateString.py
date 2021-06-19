# Given a string A, rotate the string B times in clockwise direction and return the string.
def rotateString(A, B):
    N = len(A)
    return A[-(B % N):] + A[:-(B % N)]


print(rotateString("scaler", 2))
print(rotateString("scaler", 8))
print(rotateString("academy", 7))
